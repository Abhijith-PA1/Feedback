# 🚀 Quick Start Guide

## Prerequisites
- Python 3.8+ installed
- Node.js 16+ and npm installed
- Git (optional)

---

## 🔧 Setup Instructions

### 1️⃣ Backend Setup (Flask/Python)

Open a terminal and navigate to the backend folder:

```cmd
cd backend
```

#### Create Virtual Environment
```cmd
python -m venv venv
```

#### Activate Virtual Environment
**Windows:**
```cmd
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

#### Install Dependencies
```cmd
pip install -r requirements.txt
```

#### Train ML Model (First Time Only)
```cmd
python ml_model\train_model.py
```

You should see:
```
Model trained successfully! Accuracy: 0.XX
Model saved to ...
```

#### Run Backend Server
```cmd
python app.py
```

Backend will run on: **http://localhost:5000**

---

### 2️⃣ Frontend Setup (React/Vite)

Open a **NEW terminal** (keep backend running) and navigate to frontend:

```cmd
cd frontend
```

#### Install Dependencies
```cmd
npm install
```

#### Run Development Server
```cmd
npm run dev
```

Frontend will run on: **http://localhost:5173**

---

## 🎯 Testing the Application

### 1. Open Browser
Navigate to: **http://localhost:5173**

### 2. Create User Account
- Click "Create Account"
- Fill in:
  - Name: `Test User`
  - Email: `test@example.com`
  - Password: `password123`
- Click "Create Account"

### 3. Login as User
- Email: `test@example.com`
- Password: `password123`
- You'll be redirected to `/feedback`

### 4. Submit Feedback
- Select a rating (1-5 stars)
- Write a comment (e.g., "This is amazing!")
- Click "Submit Feedback"
- The AI will analyze sentiment automatically

### 5. Login as Admin
- Logout from user account
- Login with admin credentials:
  - Email: `admin`
  - Password: `admin123`
- You'll be redirected to `/admin/dashboard`

### 6. View Admin Dashboard
- See analytics:
  - Total Users
  - Total Feedback
  - Average Rating
  - Sentiment Summary
- View all feedback with AI sentiment analysis

---

## 🛠️ Common Commands

### Backend Commands
```cmd
# Activate virtual environment
cd backend
venv\Scripts\activate

# Run backend
python app.py

# Train ML model again
python ml_model\train_model.py

# Deactivate virtual environment
deactivate
```

### Frontend Commands
```cmd
# Run development server
cd frontend
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linter
npm run lint
```

---

## 📁 Project Structure

```
project-root/
│
├── backend/                    # Flask Backend
│   ├── app.py                 # Main application
│   ├── config.py              # Configuration
│   ├── .env                   # Environment variables
│   ├── requirements.txt       # Python dependencies
│   │
│   ├── database/
│   │   └── db.py             # Database initialization
│   │
│   ├── models/
│   │   ├── user_model.py     # User model
│   │   └── feedback_model.py # Feedback model
│   │
│   ├── controllers/
│   │   ├── auth_controller.py
│   │   ├── feedback_controller.py
│   │   └── admin_controller.py
│   │
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── feedback_routes.py
│   │   └── admin_routes.py
│   │
│   ├── services/
│   │   └── sentiment_service.py
│   │
│   ├── utils/
│   │   └── auth_decorators.py
│   │
│   └── ml_model/
│       ├── train_model.py
│       └── sentiment_model.pkl
│
└── frontend/                   # React Frontend
    ├── src/
    │   ├── pages/
    │   │   ├── Signup.jsx
    │   │   ├── Login.jsx
    │   │   ├── Feedback.jsx
    │   │   └── AdminDashboard.jsx
    │   │
    │   ├── components/
    │   │   └── ProtectedRoute.jsx
    │   │
    │   ├── App.jsx
    │   └── main.jsx
    │
    ├── package.json
    └── vite.config.js
```

---

## 🔐 Default Credentials

### Admin Account (Static)
- **Email:** `admin`
- **Password:** `admin123`

### Test User Account (Create via Signup)
- **Email:** `test@example.com`
- **Password:** `password123`

---

## 🐛 Troubleshooting

### Backend Issues

**Issue:** `ModuleNotFoundError: No module named 'flask'`
```cmd
# Make sure virtual environment is activated
venv\Scripts\activate
pip install -r requirements.txt
```

**Issue:** `Warning: Sentiment model not found`
```cmd
# Train the ML model first
python ml_model\train_model.py
```

**Issue:** Port 5000 already in use
```cmd
# Change port in app.py (last line):
app.run(debug=True, port=5001)
```

### Frontend Issues

**Issue:** `npm: command not found`
- Install Node.js from https://nodejs.org/

**Issue:** Port 5173 already in use
```cmd
# Vite will automatically use next available port
# Or specify port in vite.config.js
```

**Issue:** API calls failing (CORS errors)
- Make sure backend is running on port 5000
- Check vite.config.js proxy configuration

---

## 🚀 Production Deployment

### Backend
```cmd
# Install production server
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Frontend
```cmd
# Build for production
npm run build

# Serve the dist folder with any static server
# Or deploy to Vercel, Netlify, etc.
```

---

## 📊 API Endpoints

### Authentication
- `POST /api/auth/signup` - Create new user
- `POST /api/auth/login` - Login user/admin

### Feedback
- `POST /api/feedback` - Submit feedback (JWT required)

### Admin
- `GET /api/admin/dashboard` - Get analytics (Admin JWT required)

---

## 🎓 Features

✅ User Authentication (JWT)  
✅ Role-Based Access Control  
✅ AI Sentiment Analysis (Scikit-learn)  
✅ Admin Analytics Dashboard  
✅ Responsive UI (Tailwind CSS)  
✅ Secure Password Hashing (bcrypt)  
✅ RESTful API Design  
✅ MVC Architecture  

---

## 📞 Support

If you encounter any issues:
1. Check that both backend and frontend are running
2. Verify Python and Node.js versions
3. Ensure all dependencies are installed
4. Check console for error messages

---

**Happy Coding! 🚀**
