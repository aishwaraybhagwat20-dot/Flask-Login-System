from flask import Flask, render_template, request, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            flash("Email already registered!", "danger")   # ← flash
            return redirect(url_for("register"))

        cursor.execute("""
            INSERT INTO users(name, email, password)
            VALUES(?, ?, ?)
        """, (name, email, hashed_password))

        conn.commit()
        conn.close()

        flash("Registration Successful! Please login.", "success")  # ← flash
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (username, username))
        user = cursor.fetchone()
        conn.close()

        if not user:
            flash("User not found!", "danger")         # ← flash
            return redirect(url_for("login"))

        if not check_password_hash(user[3], password):
            flash("Wrong password!", "danger")         # ← flash
            return redirect(url_for("login"))

        session["user_id"] = user[0]
        session["user_name"] = user[1]
        return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", name=session["user_name"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)