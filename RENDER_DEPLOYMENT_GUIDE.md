# 🚀 Render Deployment Guide

Complete guide to deploy your Full-Stack Feedback Management Application to Render.

---

## 📋 Prerequisites

1. **GitHub Account** - Your code must be in a GitHub repository
2. **Render Account** - Sign up at [render.com](https://render.com) (free tier available)
3. **EmotionDetection.csv** - Ensure this file is in your repository root

---

## 🏗️ Architecture Overview

Your application will be deployed as:
- **Backend API** → Render Web Service (Python/Flask)
- **Frontend** → Render Static Site (React/Vite)
- **Database** → SQLite (file-based, included in backend)
- **ML Model** → Trained during build, stored in backend

---

## 📦 Step 1: Prepare Your Repository

### 1.1 Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Prepare for Render deployment"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git push -u origin main
```

### 1.2 Verify Files

Ensure these files exist in your repository:
- ✅ `backend/requirements.txt` (with gunicorn)
- ✅ `backend/wsgi.py` (WSGI entry point)
- ✅ `backend/gunicorn_config.py` (Gunicorn config)
- ✅ `EmotionDetection.csv` (ML training data)
- ✅ `frontend/package.json` (with build script)

---

## 🔧 Step 2: Deploy Backend API

### 2.1 Create Web Service

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure the service:

**Basic Settings:**
```
Name: feedback-api
Region: Oregon (or closest to you)
Branch: main
Root Directory: backend
Runtime: Python 3
```

**Build & Deploy:**
```
Build Command: pip install -r requirements.txt && python ml_model/train_emotion_model.py
Start Command: gunicorn -c gunicorn_config.py wsgi:app
```

**Instance Type:**
```
Free (or Starter if you need more resources)
```

### 2.2 Environment Variables

Add these environment variables in Render dashboard:

| Key | Value | Notes |
|-----|-------|-------|
| `PYTHON_VERSION` | `3.11.0` | Python version |
| `SECRET_KEY` | `[Generate Random]` | Click "Generate" button |
| `JWT_SECRET_KEY` | `[Generate Random]` | Click "Generate" button |

**To generate random keys manually:**
```python
import secrets
print(secrets.token_hex(32))
```

### 2.3 Deploy

1. Click **"Create Web Service"**
2. Wait for deployment (5-10 minutes)
   - Installing dependencies
   - Training ML model (this takes time!)
   - Starting Gunicorn server
3. Note your backend URL: `https://feedback-api-xxxx.onrender.com`

### 2.4 Verify Backend

Test your API:
```bash
# Health check
curl https://your-backend-url.onrender.com/api/auth/login

# Should return 400 or 401 (means API is working)
```

---

## 🎨 Step 3: Deploy Frontend

### 3.1 Update API Configuration

Before deploying frontend, update the API URL:

**Option A: Using Environment Variable (Recommended)**

1. In Render dashboard for frontend, add environment variable:
```
VITE_API_URL=https://your-backend-url.onrender.com
```

**Option B: Hardcode (Quick but not recommended)**

Update `frontend/src/config.js`:
```javascript
const API_URL = 'https://your-backend-url.onrender.com';
export default API_URL;
```

### 3.2 Update All API Calls

You need to update all axios calls to use the config. Here's how:

**In each page file (Signup.jsx, Login.jsx, Feedback.jsx, AdminDashboard.jsx):**

```javascript
// Add this import at the top
import API_URL from '../config'

// Change axios calls from:
await axios.post('/api/auth/signup', formData)

// To:
await axios.post(`${API_URL}/api/auth/signup`, formData)
```

**Files to update:**
- `frontend/src/pages/Signup.jsx`
- `frontend/src/pages/Login.jsx`
- `frontend/src/pages/Feedback.jsx`
- `frontend/src/pages/AdminDashboard.jsx`

### 3.3 Create Static Site

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Static Site"**
3. Connect your GitHub repository
4. Configure:

**Basic Settings:**
```
Name: feedback-frontend
Branch: main
Root Directory: frontend
```

**Build Settings:**
```
Build Command: npm install && npm run build
Publish Directory: dist
```

**Environment Variables:**
```
VITE_API_URL=https://your-backend-url.onrender.com
```

### 3.4 Deploy

1. Click **"Create Static Site"**
2. Wait for deployment (2-3 minutes)
3. Your frontend URL: `https://feedback-frontend-xxxx.onrender.com`

---

## 🔐 Step 4: Configure CORS

Update `backend/app.py` to allow your frontend domain:

```python
# Change this line:
CORS(app, resources={r"/api/*": {"origins": "*"}})

# To (replace with your actual frontend URL):
CORS(app, resources={r"/api/*": {
    "origins": [
        "https://feedback-frontend-xxxx.onrender.com",
        "http://localhost:5173"  # Keep for local development
    ]
}})
```

Commit and push changes - Render will auto-deploy.

---

## ✅ Step 5: Test Your Deployment

### 5.1 Test Backend

```bash
# Test signup
curl -X POST https://your-backend-url.onrender.com/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","password":"test123"}'

# Test login
curl -X POST https://your-backend-url.onrender.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@gmail.com","password":"admin123"}'
```

### 5.2 Test Frontend

1. Visit your frontend URL
2. Try signup → Should work
3. Try login → Should work
4. Submit feedback → Should work
5. Login as admin → Should see dashboard

**Admin Credentials:**
- Email: `admin@gmail.com`
- Password: `admin123`

---

## 🎯 Step 6: Custom Domain (Optional)

### 6.1 Add Custom Domain to Frontend

1. Go to your Static Site settings
2. Click **"Custom Domains"**
3. Add your domain (e.g., `feedback.yourdomain.com`)
4. Follow DNS configuration instructions

### 6.2 Add Custom Domain to Backend

1. Go to your Web Service settings
2. Click **"Custom Domains"**
3. Add your domain (e.g., `api.yourdomain.com`)
4. Update frontend `VITE_API_URL` to use new domain

---

## 🔄 Continuous Deployment

Render automatically deploys when you push to GitHub:

```bash
# Make changes
git add .
git commit -m "Update feature"
git push origin main

# Render will automatically:
# 1. Detect the push
# 2. Rebuild and deploy
# 3. Your app is updated!
```

---

## 📊 Monitoring & Logs

### View Logs

**Backend Logs:**
1. Go to your Web Service
2. Click **"Logs"** tab
3. See real-time logs

**Frontend Logs:**
1. Go to your Static Site
2. Click **"Logs"** tab
3. See build logs

### Monitor Performance

**Metrics Available:**
- CPU usage
- Memory usage
- Request count
- Response times
- Error rates

---

## 🐛 Troubleshooting

### Backend Issues

**Problem: Build fails during ML model training**
```
Solution: Increase build timeout or use smaller dataset
- Go to Settings → Advanced
- Increase "Build Timeout" to 30 minutes
```

**Problem: App crashes with "Out of Memory"**
```
Solution: Upgrade to paid plan or optimize model
- Free tier: 512 MB RAM
- Starter: 2 GB RAM
```

**Problem: Database resets on every deploy**
```
Solution: Use PostgreSQL instead of SQLite
- SQLite is ephemeral on Render
- For persistent data, use Render PostgreSQL
```

### Frontend Issues

**Problem: API calls fail with CORS error**
```
Solution: Check CORS configuration in backend
- Ensure frontend URL is in allowed origins
- Check browser console for exact error
```

**Problem: Environment variables not working**
```
Solution: Rebuild the site
- Environment variables are baked into build
- Change requires rebuild
```

**Problem: 404 on page refresh**
```
Solution: Add redirect rules
- Create _redirects file in public folder:
  /* /index.html 200
```

---

## 💾 Database Persistence (Important!)

### Current Setup (SQLite)

⚠️ **Warning:** SQLite on Render is **ephemeral**
- Database resets on every deploy
- Data is lost when service restarts
- Only suitable for testing

### Production Setup (PostgreSQL)

For production, use PostgreSQL:

1. **Create PostgreSQL Database:**
   - Dashboard → New → PostgreSQL
   - Note the connection string

2. **Update Backend:**
   ```python
   # In config.py, change:
   SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///instance/database.db')
   
   # PostgreSQL URL format:
   # postgresql://user:password@host:port/database
   ```

3. **Add psycopg2:**
   ```
   # In requirements.txt, add:
   psycopg2-binary
   ```

4. **Set Environment Variable:**
   ```
   DATABASE_URL=postgresql://...
   ```

---

## 🚀 Performance Optimization

### Backend Optimization

1. **Use Gunicorn workers:**
   ```python
   # gunicorn_config.py
   workers = 2  # Increase for more traffic
   threads = 4
   ```

2. **Enable caching:**
   ```python
   from flask_caching import Cache
   cache = Cache(app, config={'CACHE_TYPE': 'simple'})
   ```

3. **Optimize ML model loading:**
   - Already using singleton pattern ✅
   - Model loads once and stays in memory ✅

### Frontend Optimization

1. **Enable compression:**
   - Render automatically compresses static files ✅

2. **Use CDN:**
   - Render serves from global CDN ✅

3. **Optimize images:**
   - Use WebP format
   - Compress images before upload

---

## 💰 Cost Estimation

### Free Tier (Perfect for Testing)

**Backend Web Service:**
- ✅ 750 hours/month free
- ✅ 512 MB RAM
- ✅ Sleeps after 15 min inactivity
- ⚠️ Cold starts (10-30 seconds)

**Frontend Static Site:**
- ✅ 100 GB bandwidth/month
- ✅ Global CDN
- ✅ Always on (no sleep)

**Total: $0/month**

### Paid Tier (Production Ready)

**Backend Starter:**
- $7/month
- 2 GB RAM
- Always on (no sleep)
- Faster performance

**Frontend:**
- Free (static sites are always free)

**PostgreSQL:**
- $7/month (Starter)
- 1 GB storage
- Persistent data

**Total: $14/month**

---

## 📝 Deployment Checklist

Before going live:

- [ ] Backend deployed and accessible
- [ ] Frontend deployed and accessible
- [ ] Environment variables configured
- [ ] CORS configured correctly
- [ ] ML model trained successfully
- [ ] Admin login works
- [ ] User signup works
- [ ] Feedback submission works
- [ ] Sentiment analysis works
- [ ] Admin dashboard loads
- [ ] Database persistence configured (if needed)
- [ ] Custom domain configured (optional)
- [ ] SSL certificate active (automatic)
- [ ] Monitoring enabled
- [ ] Logs accessible

---

## 🎉 Success!

Your application is now live on Render!

**URLs:**
- Frontend: `https://feedback-frontend-xxxx.onrender.com`
- Backend API: `https://feedback-api-xxxx.onrender.com`

**Next Steps:**
1. Share your app URL
2. Monitor logs for errors
3. Collect user feedback
4. Iterate and improve

---

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/2.3.x/deploying/)
- [Vite Production Build](https://vitejs.dev/guide/build.html)
- [Gunicorn Documentation](https://docs.gunicorn.org/)

---

## 🆘 Need Help?

**Render Support:**
- [Community Forum](https://community.render.com/)
- [Discord](https://discord.gg/render)
- [Email Support](mailto:support@render.com)

**Common Issues:**
- Check logs first
- Verify environment variables
- Test API endpoints manually
- Check CORS configuration
- Verify database connection

---

**Deployment Guide Version:** 1.0  
**Last Updated:** February 19, 2026  
**Status:** ✅ Production Ready
