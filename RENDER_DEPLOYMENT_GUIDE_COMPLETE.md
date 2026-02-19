# Complete Render Deployment Guide

## Prerequisites
- ✅ GitHub account with your code pushed
- ✅ Render account (free tier works)
- ✅ Your repository: https://github.com/Abhijith-PA1/Feedback

---

## Part 1: Create PostgreSQL Database

### Step 1: Go to Render Dashboard
1. Open https://dashboard.render.com
2. Log in to your account

### Step 2: Create Database
1. Click **"New +"** button (top right)
2. Select **"PostgreSQL"**
3. Fill in the details:
   - **Name:** `feedback-db`
   - **Database:** `feedback_db`
   - **User:** `feedback_user` (or leave default)
   - **Region:** `Oregon (US West)`
   - **PostgreSQL Version:** `16` (or latest)
   - **Plan:** `Free`
4. Click **"Create Database"**
5. Wait 2-3 minutes for database to be created
6. ✅ Database is ready when status shows "Available"

---

## Part 2: Deploy Backend API

### Step 3: Create Web Service
1. Click **"New +"** button again
2. Select **"Web Service"**

### Step 4: Connect GitHub Repository
1. Click **"Connect a repository"**
2. If first time: Click **"Configure account"** to authorize Render
3. Select your repository: **"Abhijith-PA1/Feedback"**
4. Click **"Connect"**

### Step 5: Configure Service Settings

Fill in these EXACT values:

**Basic Settings:**
- **Name:** `feedback-api`
- **Region:** `Oregon (US West)`
- **Branch:** `main`
- **Root Directory:** Leave EMPTY (we use cd in commands)
- **Runtime:** `Python 3`

**Build & Deploy Settings:**
- **Build Command:**
  ```
  cd backend && pip install -r requirements.txt && python ml_model/train_emotion_model.py
  ```

- **Start Command:**
  ```
  cd backend && gunicorn wsgi:app
  ```

**Instance Type:**
- Select **"Free"** (or your preferred plan)

### Step 6: Add Environment Variables

Click **"Add Environment Variable"** for each:

1. **SECRET_KEY**
   - Click "Generate" button (Render will create a random key)

2. **JWT_SECRET_KEY**
   - Click "Generate" button (Render will create a random key)

3. **DATABASE_URL**
   - Click dropdown and select **"feedback-db"** (the database you created)
   - Render will automatically link it

4. **PYTHON_VERSION**
   - Value: `3.11.0`

5. **FLASK_ENV** (optional, for clarity)
   - Value: `production`

### Step 7: Create Service
1. Review all settings
2. Click **"Create Web Service"** button
3. Render will start building your app

---

## Part 3: Monitor Deployment

### Step 8: Watch Build Logs
You'll see logs like:
```
==> Cloning from https://github.com/Abhijith-PA1/Feedback
==> Checking out commit...
==> Running build command...
==> Installing dependencies...
==> Training ML model...
==> Build succeeded ✓
==> Starting service...
==> Your service is live 🎉
```

**Build takes 3-5 minutes**

### Step 9: Verify Deployment
1. Once deployed, you'll see a URL like: `https://feedback-backend-x85o.onrender.com`
2. Click on the URL
3. Test an endpoint: `https://feedback-backend-x85o.onrender.com/api/auth/login`

---

## Part 4: Update Frontend (If Needed)

### Step 10: Update Frontend API URL
If you have a frontend, update the API URL:

1. Open `frontend/.env.production`
2. Update:
   ```
   VITE_API_URL=https://feedback-backend-x85o.onrender.com
   ```
3. Commit and push changes

---

## Troubleshooting

### If Build Fails with "requirements.txt not found"
**Solution:** Make sure Build Command includes `cd backend`:
```
cd backend && pip install -r requirements.txt && python ml_model/train_emotion_model.py
```

### If Service Crashes on Start
**Check:**
1. Start Command is correct: `cd backend && gunicorn wsgi:app`
2. All environment variables are set
3. Database is connected

### If Database Connection Fails
**Check:**
1. DATABASE_URL is linked to your database
2. Database status is "Available"
3. Check logs for connection errors

### View Logs
1. Go to your service in Render
2. Click **"Logs"** tab
3. Look for error messages

---

## Important Notes

### Free Tier Limitations
- Service spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- Database has 90-day expiration (free tier)

### Keep Service Active
To prevent spin-down, use a service like:
- UptimeRobot (free)
- Cron-job.org (free)
- Ping your API every 10 minutes

### Upgrade for Production
For production use, consider:
- Paid plan ($7/month) - no spin-down
- Larger database plan
- Custom domain

---

## Quick Reference

**Your URLs:**
- Backend API: `https://feedback-backend-x85o.onrender.com`
- Database: Internal connection via DATABASE_URL

**Important Commands:**
- Build: `cd backend && pip install -r requirements.txt && python ml_model/train_emotion_model.py`
- Start: `cd backend && gunicorn wsgi:app`

**Environment Variables:**
- SECRET_KEY (auto-generated)
- JWT_SECRET_KEY (auto-generated)
- DATABASE_URL (linked to database)
- PYTHON_VERSION: 3.11.0

---

## Next Steps After Deployment

1. ✅ Test all API endpoints
2. ✅ Verify database connections
3. ✅ Update frontend to use new API URL
4. ✅ Set up monitoring/uptime checks
5. ✅ Configure custom domain (optional)

---

## Need Help?

If you encounter issues:
1. Check Render logs
2. Verify all environment variables
3. Ensure database is connected
4. Check GitHub repository has latest code

**Common Issues:**
- Build fails → Check build command
- Service crashes → Check start command and logs
- Database errors → Verify DATABASE_URL is set
- 404 errors → Check API routes and CORS settings
