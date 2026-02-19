# 🏗️ Deployment Architecture

Visual guide to understand how your app is deployed on Render.

---

## 📊 Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         USERS                                │
│                    (Web Browsers)                            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ HTTPS
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
┌───────────────┐         ┌──────────────┐
│   FRONTEND    │         │   BACKEND    │
│  Static Site  │────────▶│  Web Service │
│               │  API    │              │
│  React + Vite │  Calls  │ Flask + ML   │
└───────────────┘         └──────┬───────┘
        │                        │
        │                        │
        ▼                        ▼
┌───────────────┐         ┌──────────────┐
│  Render CDN   │         │   SQLite DB  │
│  (Global)     │         │  (Ephemeral) │
└───────────────┘         └──────────────┘
```

---

## 🔄 Request Flow

### 1. User Visits Website
```
User Browser
    ↓
Render CDN (Global)
    ↓
Frontend Static Files (HTML/CSS/JS)
    ↓
User sees React App
```

### 2. User Submits Feedback
```
User fills form
    ↓
React sends POST request
    ↓
Backend API receives request
    ↓
ML Model analyzes sentiment
    ↓
Data saved to SQLite
    ↓
Response sent back to frontend
    ↓
User sees success message
```

### 3. Admin Views Dashboard
```
Admin logs in
    ↓
JWT token generated
    ↓
Frontend requests dashboard data
    ↓
Backend verifies JWT
    ↓
Backend queries database
    ↓
Aggregated data returned
    ↓
Admin sees analytics
```

---

## 🌐 Deployment Components

### Frontend (Static Site)
```
┌─────────────────────────────────┐
│  Render Static Site             │
├─────────────────────────────────┤
│  • React Application            │
│  • Vite Build Output            │
│  • Served from Global CDN       │
│  • Always On (No Sleep)         │
│  • HTTPS Automatic              │
│  • Custom Domain Support        │
└─────────────────────────────────┘
```

**Features:**
- ✅ Instant loading (CDN)
- ✅ No cold starts
- ✅ 100 GB bandwidth/month (free)
- ✅ Automatic SSL certificate

### Backend (Web Service)
```
┌─────────────────────────────────┐
│  Render Web Service             │
├─────────────────────────────────┤
│  • Flask Application            │
│  • Gunicorn WSGI Server         │
│  • ML Model (In-Memory)         │
│  • SQLite Database              │
│  • JWT Authentication           │
│  • RESTful API                  │
└─────────────────────────────────┘
```

**Features:**
- ✅ Python 3.11
- ✅ 512 MB RAM (free tier)
- ✅ Auto-deploy on git push
- ⚠️ Sleeps after 15 min (free tier)
- ⚠️ Cold start: 10-30 seconds

---

## 💾 Data Flow

### Feedback Submission Flow
```
1. User Input
   ↓
2. Frontend Validation
   ↓
3. API Request (POST /api/feedback)
   ↓
4. Backend Receives Data
   ↓
5. JWT Verification
   ↓
6. ML Sentiment Analysis
   ↓
7. Database Insert
   ↓
8. Response to Frontend
   ↓
9. Success Message to User
```

### ML Model Flow
```
1. Build Time
   ├─ Load EmotionDetection.csv (839K samples)
   ├─ Train TF-IDF Vectorizer
   ├─ Train Logistic Regression
   └─ Save model.pkl (5 MB)

2. Runtime
   ├─ Load model once (singleton)
   ├─ Keep in memory
   └─ Predict sentiment for each feedback
```

---

## 🔐 Security Architecture

```
┌─────────────────────────────────────────┐
│           Security Layers               │
├─────────────────────────────────────────┤
│  1. HTTPS/SSL (Automatic)               │
│     └─ All traffic encrypted            │
│                                         │
│  2. CORS (Backend)                      │
│     └─ Only allowed origins             │
│                                         │
│  3. JWT Authentication                  │
│     └─ Stateless auth tokens            │
│                                         │
│  4. Password Hashing (bcrypt)           │
│     └─ Passwords never stored plain     │
│                                         │
│  5. Environment Variables               │
│     └─ Secrets not in code              │
└─────────────────────────────────────────┘
```

---

## 📦 Build Process

### Backend Build
```
1. Git Push
   ↓
2. Render Detects Change
   ↓
3. Install Dependencies (pip)
   ├─ Flask
   ├─ Gunicorn
   ├─ Scikit-learn
   └─ Other packages
   ↓
4. Train ML Model
   ├─ Load CSV (839K samples)
   ├─ Train model (2-3 minutes)
   └─ Save model.pkl
   ↓
5. Start Gunicorn
   ├─ Load Flask app
   ├─ Load ML model
   └─ Listen on port 5000
   ↓
6. Health Check
   ↓
7. Deploy Complete ✅
```

**Time:** 5-10 minutes

### Frontend Build
```
1. Git Push
   ↓
2. Render Detects Change
   ↓
3. Install Dependencies (npm)
   ├─ React
   ├─ Vite
   ├─ Tailwind
   └─ Other packages
   ↓
4. Build Production Bundle
   ├─ Optimize code
   ├─ Minify assets
   ├─ Generate static files
   └─ Output to /dist
   ↓
5. Deploy to CDN
   ↓
6. Deploy Complete ✅
```

**Time:** 2-3 minutes

---

## 🔄 Auto-Deploy Workflow

```
Developer                 GitHub              Render
    │                        │                  │
    │  git push              │                  │
    ├───────────────────────▶│                  │
    │                        │  Webhook         │
    │                        ├─────────────────▶│
    │                        │                  │
    │                        │              Build & Deploy
    │                        │                  │
    │                        │  Deploy Complete │
    │                        │◀─────────────────┤
    │                        │                  │
    │  App Updated! ✅       │                  │
    │◀───────────────────────┴──────────────────┤
```

---

## 💰 Cost Breakdown

### Free Tier (Perfect for Testing)
```
┌─────────────────────────────────┐
│  Frontend Static Site           │
│  • 100 GB bandwidth             │
│  • Global CDN                   │
│  • Always on                    │
│  Cost: $0/month                 │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  Backend Web Service            │
│  • 750 hours/month              │
│  • 512 MB RAM                   │
│  • Sleeps after 15 min          │
│  Cost: $0/month                 │
└─────────────────────────────────┘

Total: $0/month ✅
```

### Paid Tier (Production Ready)
```
┌─────────────────────────────────┐
│  Frontend Static Site           │
│  • Unlimited bandwidth          │
│  • Global CDN                   │
│  • Always on                    │
│  Cost: $0/month                 │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  Backend Starter                │
│  • Always on (no sleep)         │
│  • 2 GB RAM                     │
│  • Better performance           │
│  Cost: $7/month                 │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  PostgreSQL Database            │
│  • 1 GB storage                 │
│  • Persistent data              │
│  • Automatic backups            │
│  Cost: $7/month                 │
└─────────────────────────────────┘

Total: $14/month
```

---

## 🚀 Performance Characteristics

### Frontend Performance
```
Metric              Free Tier    Paid Tier
─────────────────────────────────────────
First Load          < 1 second   < 1 second
Page Navigation     Instant      Instant
API Calls           Depends      Depends
CDN Latency         < 50ms       < 50ms
Availability        99.9%        99.9%
```

### Backend Performance
```
Metric              Free Tier    Paid Tier
─────────────────────────────────────────
Cold Start          10-30 sec    N/A
Warm Response       < 200ms      < 100ms
ML Prediction       < 50ms       < 50ms
Database Query      < 10ms       < 10ms
Availability        99%          99.9%
```

---

## 🎯 Scaling Strategy

### Current Setup (Free Tier)
```
Users: 1-100 concurrent
Traffic: Low to moderate
Cost: $0/month
Suitable for: Testing, demos, small projects
```

### Scaled Setup (Paid Tier)
```
Users: 100-1000 concurrent
Traffic: Moderate to high
Cost: $14/month
Suitable for: Production, real users
```

### Enterprise Setup
```
Users: 1000+ concurrent
Traffic: High
Cost: $50+/month
Features:
  • Multiple backend instances
  • Load balancing
  • Larger database
  • Priority support
```

---

## 📊 Monitoring & Observability

### Available Metrics
```
Frontend:
  • Build status
  • Deploy history
  • Bandwidth usage
  • Error logs

Backend:
  • CPU usage
  • Memory usage
  • Request count
  • Response times
  • Error rates
  • Logs (real-time)
```

### Health Checks
```
Frontend:
  ✅ Automatic (CDN)

Backend:
  ✅ HTTP health endpoint
  ✅ Auto-restart on failure
  ✅ Email alerts
```

---

## 🔧 Maintenance

### Automatic
- ✅ SSL certificate renewal
- ✅ Security patches
- ✅ Platform updates
- ✅ CDN optimization

### Manual
- 🔄 Dependency updates
- 🔄 Code deployments
- 🔄 Database migrations
- 🔄 Configuration changes

---

## 📈 Growth Path

```
Stage 1: Development
  • Local development
  • SQLite database
  • Manual testing

Stage 2: Testing (Free Tier)
  • Deploy to Render
  • Share with testers
  • Gather feedback

Stage 3: Production (Paid Tier)
  • Upgrade to Starter
  • Add PostgreSQL
  • Custom domain
  • Monitor metrics

Stage 4: Scale
  • Multiple instances
  • Load balancing
  • Caching layer
  • Advanced monitoring
```

---

**Ready to deploy?** Follow `DEPLOYMENT_CHECKLIST.md`! 🚀
