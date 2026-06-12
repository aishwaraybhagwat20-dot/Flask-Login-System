import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM users WHERE email = ?", ("aishwaraybhagwat20@gmail.com",))

conn.commit()
conn.close()

print(f"Deleted {cursor.rowcount} user(s)")