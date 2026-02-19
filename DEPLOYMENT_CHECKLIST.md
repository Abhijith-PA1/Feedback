# Render Deployment Checklist

## Quick Start Checklist

### Before You Start
- [ ] GitHub repository is up to date
- [ ] You have a Render account (sign up at render.com)
- [ ] You're logged into Render dashboard

---

## Database Setup (5 minutes)

- [ ] Go to https://dashboard.render.com
- [ ] Click "New +" → "PostgreSQL"
- [ ] Name: `feedback-db`
- [ ] Region: Oregon (US West)
- [ ] Plan: Free
- [ ] Click "Create Database"
- [ ] Wait for status: "Available" ✅

---

## Backend Deployment (10 minutes)

- [ ] Click "New +" → "Web Service"
- [ ] Connect repository: `Abhijith-PA1/Feedback`
- [ ] Configure settings:

### Basic Info
- [ ] Name: `feedback-api`
- [ ] Region: Oregon (US West)
- [ ] Branch: `main`
- [ ] Runtime: Python 3

### Commands (COPY EXACTLY)
- [ ] Build Command:
  ```
  cd backend && pip install -r requirements.txt && python ml_model/train_emotion_model.py
  ```

- [ ] Start Command:
  ```
  cd backend && gunicorn wsgi:app
  ```

### Environment Variables
- [ ] SECRET_KEY → Click "Generate"
- [ ] JWT_SECRET_KEY → Click "Generate"
- [ ] DATABASE_URL → Select "feedback-db"
- [ ] PYTHON_VERSION → Enter: `3.11.0`

### Deploy
- [ ] Click "Create Web Service"
- [ ] Wait 3-5 minutes for build
- [ ] Check logs for "Your service is live" ✅

---

## Verification (2 minutes)

- [ ] Copy your service URL (e.g., `https://feedback-api.onrender.com`)
- [ ] Test in browser: `https://your-url.onrender.com/api/auth/login`
- [ ] Should see JSON response (not 404)
- [ ] Check logs for any errors

---

## Done! 🎉

Your backend is now live at: `https://feedback-api.onrender.com`

### Next Steps:
- [ ] Update frontend API URL (if you have one)
- [ ] Test all endpoints
- [ ] Set up uptime monitoring (optional)
- [ ] Configure custom domain (optional)

---

## If Something Goes Wrong

### Build Fails?
→ Check that Build Command includes `cd backend`

### Service Crashes?
→ Check Start Command and environment variables

### Database Errors?
→ Verify DATABASE_URL is linked to feedback-db

### Still Stuck?
→ Check the logs in Render dashboard
→ Refer to RENDER_DEPLOYMENT_GUIDE_COMPLETE.md
