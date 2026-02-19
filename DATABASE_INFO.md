# 📊 Database Information

## 🗄️ Where User Data is Stored

### Database Location
**File:** `backend/instance/database.db`  
**Type:** SQLite Database  
**Size:** ~16 KB  
**Format:** Binary SQLite3 file

### Full Path
```
C:\Users\Abhijith\Desktop\mt\backend\instance\database.db
```

---

## 📋 Database Structure

### Tables

#### 1. **users** Table
Stores all user account information:

| Column   | Type    | Description                    |
|----------|---------|--------------------------------|
| id       | INTEGER | Primary key (auto-increment)   |
| name     | STRING  | User's full name               |
| email    | STRING  | User's email (unique)          |
| password | STRING  | Hashed password (bcrypt)       |
| role     | STRING  | User role (default: "user")    |

**Example Data:**
```
id: 1
name: "Test User"
email: "test@example.com"
password: "$2b$12$..." (hashed)
role: "user"
```

#### 2. **feedbacks** Table
Stores all feedback submissions:

| Column    | Type    | Description                        |
|-----------|---------|------------------------------------|
| id        | INTEGER | Primary key (auto-increment)       |
| user_id   | INTEGER | Foreign key to users.id            |
| rating    | INTEGER | Rating (1-5)                       |
| comment   | TEXT    | Feedback comment                   |
| sentiment | STRING  | AI predicted sentiment             |

**Example Data:**
```
id: 1
user_id: 1
rating: 5
comment: "This is amazing!"
sentiment: "positive"
```

---

## 🔗 Relationships

```
users (1) ----< (many) feedbacks
  |
  └─ One user can have many feedbacks
```

**SQLAlchemy Relationship:**
```python
# In User model
feedbacks = db.relationship('Feedback', backref='user', lazy=True)

# In Feedback model
user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
```

---

## 🔍 How to View Database

### Option 1: Using SQLite Browser (Recommended)
1. Download **DB Browser for SQLite**: https://sqlitebrowser.org/
2. Open the file: `backend/instance/database.db`
3. Browse tables, view data, run queries

### Option 2: Using Python Script
Create a file `view_database.py` in backend folder:

```python
import sqlite3

# Connect to database
conn = sqlite3.connect('instance/database.db')
cursor = conn.cursor()

# View all users
print("=== USERS ===")
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

print("\n=== FEEDBACKS ===")
cursor.execute("SELECT * FROM feedbacks")
for row in cursor.fetchall():
    print(row)

conn.close()
```

Run with:
```cmd
cd backend
.\venv\Scripts\activate
python view_database.py
```

### Option 3: Using SQLite Command Line
```cmd
cd backend\instance
sqlite3 database.db

# Inside SQLite shell:
.tables                    # List all tables
SELECT * FROM users;       # View all users
SELECT * FROM feedbacks;   # View all feedbacks
.exit                      # Exit
```

---

## 🔐 Security Features

### Password Storage
- **NOT stored in plain text**
- **Hashed using bcrypt** with salt
- Example: `$2b$12$abcd1234...` (60 characters)
- Cannot be reversed to get original password

### Admin Account
- **Static credentials** (not in database)
- Email: `admin@gmail.com`
- Password: `admin123`
- Handled in code, not stored in database

---

## 📊 Current Database Content

Based on recent API calls, your database contains:
- ✅ User accounts (created via signup)
- ✅ Feedback submissions with ratings
- ✅ AI sentiment analysis results

---

## 🔄 Database Operations

### When Data is Created

#### User Registration (Signup)
```python
# File: backend/controllers/auth_controller.py
new_user = User(
    name=name,
    email=email,
    password=hashed_password,
    role='user'
)
db.session.add(new_user)
db.session.commit()
```

#### Feedback Submission
```python
# File: backend/controllers/feedback_controller.py
new_feedback = Feedback(
    user_id=int(user_id),
    rating=rating,
    comment=comment,
    sentiment=sentiment
)
db.session.add(new_feedback)
db.session.commit()
```

### When Data is Read

#### Admin Dashboard
```python
# File: backend/controllers/admin_controller.py
total_users = User.query.count()
total_feedback = Feedback.query.count()
feedbacks = db.session.query(Feedback, User).join(User).all()
```

---

## 🗑️ How to Reset Database

If you want to start fresh:

### Option 1: Delete Database File
```cmd
# Stop the backend server first!
cd backend
del instance\database.db

# Restart backend - it will create a new empty database
python app.py
```

### Option 2: Using Python Script
Create `reset_database.py`:

```python
from app import create_app
from database.db import db

app = create_app()
with app.app_context():
    db.drop_all()  # Delete all tables
    db.create_all()  # Recreate empty tables
    print("Database reset successfully!")
```

Run with:
```cmd
cd backend
.\venv\Scripts\activate
python reset_database.py
```

---

## 📈 Database Growth

### Current Size: ~16 KB

**Estimated Growth:**
- Each user: ~200 bytes
- Each feedback: ~500 bytes (depends on comment length)

**Example:**
- 100 users + 1000 feedbacks ≈ 520 KB
- 1000 users + 10000 feedbacks ≈ 5 MB

SQLite can handle databases up to **281 TB**, so you're good! 😄

---

## 🚀 Production Considerations

### For Production Deployment:

1. **Switch to PostgreSQL or MySQL**
   - SQLite is great for development
   - Use PostgreSQL for production (better concurrency)

2. **Add Database Backups**
   ```cmd
   # Backup SQLite
   copy backend\instance\database.db backup_YYYYMMDD.db
   ```

3. **Add Database Migrations**
   - Use Flask-Migrate
   - Track schema changes
   - Version control for database

4. **Environment-Specific Databases**
   - Development: SQLite
   - Staging: PostgreSQL
   - Production: PostgreSQL with backups

---

## 📝 Summary

**Location:** `backend/instance/database.db`  
**Type:** SQLite3  
**Tables:** users, feedbacks  
**Security:** Passwords hashed with bcrypt  
**Access:** SQLite Browser, Python, or SQLite CLI  

Your data is safely stored and properly secured! 🔒
