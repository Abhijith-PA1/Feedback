# 📊 Feedback & Rating Storage Guide

**System:** Feedback Management Application  
**Database:** SQLite  
**Location:** `backend/instance/database.db`

---

## 🗄️ Where Feedback is Stored

### Database File Location
```
C:\Users\Abhijith\Desktop\mt\backend\instance\database.db
```

### Database Type
- **SQLite** - File-based relational database
- **Size:** ~16 KB (grows with data)
- **Format:** Binary database file

---

## 📋 Database Schema

### Table: `feedbacks`

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| **id** | INTEGER | Primary key (auto-increment) | 1, 2, 3... |
| **user_id** | INTEGER | Foreign key to users table | 5 |
| **rating** | INTEGER | Star rating (1-5) | 5 |
| **comment** | TEXT | User's feedback text | "Great product!" |
| **sentiment** | STRING | AI-predicted sentiment | "positive" |

### Table: `users`

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| **id** | INTEGER | Primary key (auto-increment) | 1, 2, 3... |
| **name** | STRING | User's full name | "John Doe" |
| **email** | STRING | User's email (unique) | "john@example.com" |
| **password** | STRING | Hashed password | "$2b$12$..." |
| **role** | STRING | User role | "user" or "admin" |

---

## 🔄 Data Flow: How Feedback is Saved

### Step-by-Step Process

#### 1. User Submits Feedback (Frontend)
```javascript
// File: frontend/src/pages/Feedback.jsx
const handleSubmit = async (e) => {
    const token = localStorage.getItem('token')
    const res = await axios.post(
        '/api/feedback',
        { 
            rating: parseInt(rating),  // e.g., 5
            comment: comment           // e.g., "Great product!"
        },
        { headers: { Authorization: `Bearer ${token}` } }
    )
}
```

**Data Sent:**
```json
{
  "rating": 5,
  "comment": "Great product!"
}
```

---

#### 2. Backend Receives Request
```python
# File: backend/controllers/feedback_controller.py
@jwt_required()
def submit_feedback():
    data = request.get_json()
    rating = data.get('rating')      # 5
    comment = data.get('comment')    # "Great product!"
    user_id = get_jwt_identity()     # From JWT token
```

---

#### 3. AI Analyzes Sentiment
```python
# File: backend/services/sentiment_service.py
sentiment = predict_sentiment(comment)
# Input: "Great product!"
# Output: "positive"
```

---

#### 4. Data Saved to Database
```python
# File: backend/controllers/feedback_controller.py
new_feedback = Feedback(
    user_id=int(user_id),      # 5
    rating=rating,             # 5
    comment=comment,           # "Great product!"
    sentiment=sentiment        # "positive"
)
db.session.add(new_feedback)
db.session.commit()
```

**SQL Executed:**
```sql
INSERT INTO feedbacks (user_id, rating, comment, sentiment)
VALUES (5, 5, 'Great product!', 'positive');
```

---

#### 5. Database Stores Record

**Stored in:** `backend/instance/database.db`

**Table:** `feedbacks`

| id | user_id | rating | comment | sentiment |
|----|---------|--------|---------|-----------|
| 1 | 5 | 5 | "Great product!" | positive |

---

## 📊 Example: Complete Feedback Record

### User Information (from `users` table)
```json
{
  "id": 5,
  "name": "John Doe",
  "email": "john@example.com",
  "role": "user"
}
```

### Feedback Information (from `feedbacks` table)
```json
{
  "id": 1,
  "user_id": 5,
  "rating": 5,
  "comment": "Great product!",
  "sentiment": "positive"
}
```

### Combined View (Admin Dashboard)
```json
{
  "id": 1,
  "userName": "John Doe",
  "rating": 5,
  "comment": "Great product!",
  "sentiment": "positive"
}
```

---

## 🔍 How to View Stored Data

### Method 1: Using DB Browser for SQLite (Recommended)

1. **Download:** https://sqlitebrowser.org/
2. **Open:** `backend/instance/database.db`
3. **Browse Data:** Click "Browse Data" tab
4. **Select Table:** Choose "feedbacks" or "users"

**Screenshot of what you'll see:**
```
┌────┬─────────┬────────┬──────────────────┬───────────┐
│ id │ user_id │ rating │ comment          │ sentiment │
├────┼─────────┼────────┼──────────────────┼───────────┤
│ 1  │ 5       │ 5      │ Great product!   │ positive  │
│ 2  │ 5       │ 4      │ Pretty good      │ positive  │
│ 3  │ 6       │ 2      │ Not satisfied    │ negative  │
└────┴─────────┴────────┴──────────────────┴───────────┘
```

---

### Method 2: Using Python Script

Create `backend/view_feedback.py`:
```python
import sqlite3

# Connect to database
conn = sqlite3.connect('instance/database.db')
cursor = conn.cursor()

# Query all feedback with user names
query = """
SELECT 
    f.id,
    u.name as user_name,
    u.email,
    f.rating,
    f.comment,
    f.sentiment
FROM feedbacks f
JOIN users u ON f.user_id = u.id
ORDER BY f.id DESC
"""

cursor.execute(query)
results = cursor.fetchall()

print("=" * 80)
print("ALL FEEDBACK RECORDS")
print("=" * 80)

for row in results:
    print(f"\nID: {row[0]}")
    print(f"User: {row[1]} ({row[2]})")
    print(f"Rating: {'⭐' * row[3]} ({row[3]}/5)")
    print(f"Comment: {row[4]}")
    print(f"Sentiment: {row[5]}")
    print("-" * 80)

conn.close()
```

**Run:**
```cmd
cd backend
.\venv\Scripts\activate
python view_feedback.py
```

---

### Method 3: Using SQLite Command Line

```cmd
cd backend\instance
sqlite3 database.db

-- View all feedback
SELECT * FROM feedbacks;

-- View feedback with user names
SELECT 
    f.id,
    u.name,
    f.rating,
    f.comment,
    f.sentiment
FROM feedbacks f
JOIN users u ON f.user_id = u.id;

-- Exit
.exit
```

---

### Method 4: Using Admin Dashboard (Web UI)

1. **Login as admin:**
   - Email: `admin@gmail.com`
   - Password: `admin123`

2. **View Dashboard:**
   - URL: http://localhost:5173/admin/dashboard
   - See all feedback in a table
   - View analytics and sentiment breakdown

---

## 📈 Data Relationships

### Database Relationship Diagram

```
┌─────────────────┐         ┌──────────────────┐
│     users       │         │    feedbacks     │
├─────────────────┤         ├──────────────────┤
│ id (PK)         │◄────────│ id (PK)          │
│ name            │    1:N  │ user_id (FK)     │
│ email           │         │ rating           │
│ password        │         │ comment          │
│ role            │         │ sentiment        │
└─────────────────┘         └──────────────────┘
```

**Relationship:** One user can have many feedbacks

---

## 🔐 Data Security

### Password Storage
- **NOT stored in plain text**
- **Hashed with bcrypt**
- Example: `$2b$12$abcd1234...` (60 characters)

### Feedback Storage
- **Plain text** (comment is readable)
- **Associated with user** (via user_id)
- **Includes AI analysis** (sentiment)

---

## 📊 Storage Statistics

### Current Database
```
File: backend/instance/database.db
Size: ~16 KB
Tables: 2 (users, feedbacks)
Indexes: 5 (optimized for fast queries)
```

### Growth Estimation
- Each user: ~200 bytes
- Each feedback: ~500 bytes (depends on comment length)

**Examples:**
- 100 users + 1,000 feedbacks ≈ 520 KB
- 1,000 users + 10,000 feedbacks ≈ 5 MB
- 10,000 users + 100,000 feedbacks ≈ 50 MB

---

## 🔄 Data Lifecycle

### 1. Creation
```
User submits feedback → API validates → AI analyzes → Database stores
```

### 2. Reading
```
Admin requests dashboard → Database queries → API returns → UI displays
```

### 3. Updates
```
Currently: No update functionality
Future: Could add edit/delete features
```

### 4. Deletion
```
Currently: No delete functionality
Future: Could add admin delete feature
```

---

## 🛠️ Database Operations

### View All Feedback (SQL)
```sql
SELECT * FROM feedbacks;
```

### View Feedback with User Info (SQL)
```sql
SELECT 
    f.id,
    u.name,
    u.email,
    f.rating,
    f.comment,
    f.sentiment
FROM feedbacks f
JOIN users u ON f.user_id = u.id
ORDER BY f.id DESC;
```

### Count Feedback by Sentiment (SQL)
```sql
SELECT 
    sentiment,
    COUNT(*) as count
FROM feedbacks
GROUP BY sentiment;
```

### Average Rating (SQL)
```sql
SELECT AVG(rating) as average_rating
FROM feedbacks;
```

---

## 📁 File Structure

```
backend/
├── instance/
│   └── database.db          ← FEEDBACK STORED HERE
├── models/
│   ├── user_model.py        ← User table definition
│   └── feedback_model.py    ← Feedback table definition
├── controllers/
│   └── feedback_controller.py  ← Saves feedback
└── services/
    └── sentiment_service.py    ← AI analysis
```

---

## 🎯 Summary

### Where is feedback stored?
**File:** `C:\Users\Abhijith\Desktop\mt\backend\instance\database.db`

### What is stored?
- User ID (who submitted)
- Rating (1-5 stars)
- Comment (text)
- Sentiment (AI prediction)

### How to view it?
1. DB Browser for SQLite (GUI)
2. Python script
3. SQLite command line
4. Admin dashboard (web UI)

### Is it secure?
- ✅ Passwords hashed
- ✅ JWT authentication
- ✅ Role-based access
- ⚠️ Comments stored in plain text

---

**Need to view your feedback data? Use any of the 4 methods above!** 📊
