# Flask Login System

A complete user authentication system built with Python and Flask. This project was built as a learning exercise to understand backend web development, database management, and session handling.

## Features
- User Registration
- Password Hashing using Werkzeug
- Duplicate email prevention
- Login with email or username
- Session Management
- Protected dashboard route
- Logout functionality
- Flash messages for errors and success
- Bootstrap 5 UI

## Tech Stack
- Python 3
- Flask
- SQLite
- Bootstrap 5
- Werkzeug Security

## Setup and Installation

1. Clone the repo
\```
git clone https://github.com/aishwaraybhagwat20-dot/Flask-Login-System.git
\```

2. Create virtual environment
\```
python -m venv venv
source venv/bin/activate
\```

3. Install dependencies
\```
pip install -r requirements.txt
\```

4. Create database
\```
python create_db.py
\```

5. Run the app
\```
python app.py
\```

6. Open in browser
\```
http://127.0.0.1:5000
\```

## Project Structure
\```
Flask-Login-System/
│
├── app.py
├── create_db.py
├── clear_user.py
├── show_user.py
├── requirements.txt
├── README.md
│
└── templates/
    ├── index.html
    ├── register.html
    ├── login.html
    └── dashboard.html
\```

## How It Works
1. User registers with name, email and password
2. Password is hashed before storing in database
3. On login, password is verified using check_password_hash
4. Session is created on successful login
5. Dashboard is protected, only accessible when logged in
6. Logout destroys the session
