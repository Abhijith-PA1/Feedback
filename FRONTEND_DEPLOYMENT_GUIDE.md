# Frontend Deployment Guide - Render

## Step-by-Step Guide to Deploy React Frontend

### Prerequisites
- ✅ Backend is deployed: https://feedback-backend-x85o.onrender.com
- ✅ GitHub repository is up to date
- ✅ Render account

---

## Method 1: Deploy via Render Dashboard (Recommended)

### Step 1: Go to Render Dashboard
1. Open https://dashboard.render.com
2. Log in to your account

### Step 2: Create Static Site
1. Click **"New +"** button (top right)
2. Select **"Static Site"**

### Step 3: Connect Repository
1. Click **"Connect a repository"**
2. Select: **"Abhijith-PA1/Feedback"**
3. Click **"Connect"**

### Step 4: Configure Static Site Settings

Fill in these EXACT values:

**Basic Settings:**
- **Name:** `feedback-frontend`
- **Region:** `Oregon (US West)`
- **Branch:** `main`
- **Root Directory:** `frontend`

**Build Settings:**
- **Build Command:**
  ```
  npm install && npm run build
  ```

- **Publish Directory:**
  ```
  dist
  ```

**Environment Variables:**
Click **"Add Environment Variable"**:
- **Key:** `VITE_API_URL`
- **Value:** `https://feedback-backend-x85o.onrender.com`

### Step 5: Create Static Site
1. Review all settings
2. Click **"Create Static Site"** button
3. Render will start building your frontend

### Step 6: Wait for Deployment
- Build takes 2-3 minutes
- Watch the logs for any errors
- Once complete, you'll get a URL like: `https://feedback-frontend-3mdn.onrender.com`

---

## Method 2: Deploy Using render.yaml (Alternative)

The `render.yaml` file has been updated to include frontend configuration.

### If Using render.yaml:
1. Commit and push the updated `render.yaml`
2. In Render dashboard, create a new service
3. Select **"Use render.yaml"**
4. Render will automatically configure both backend and frontend

---

## Verification Steps

### Step 1: Test Your Frontend
1. Open your frontend URL: `https://feedback-frontend-3mdn.onrender.com`
2. You should see your app's homepage

### Step 2: Test Backend Connection
1. Try to sign up with a test account
2. Try to log in
3. Submit feedback
4. Check if data is being saved

### Step 3: Check Browser Console
1. Open browser DevTools (F12)
2. Go to Console tab
3. Look for any errors
4. Check Network tab for API calls

---

## Troubleshooting

### Build Fails

**Error: "Cannot find module"**
- Solution: Make sure `package.json` is in the `frontend` folder
- Check Root Directory is set to `frontend`

**Error: "npm command not found"**
- Solution: Render should auto-detect Node.js
- Try changing Build Command to: `cd frontend && npm install && npm run build`

### Site Loads but API Calls Fail

**Check CORS:**
Your backend should have CORS enabled (already configured):
```python
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

**Check Environment Variable:**
- Go to frontend service → Environment tab
- Verify `VITE_API_URL` is set correctly
- Value should be: `https://feedback-backend-x85o.onrender.com`

**Check Network Tab:**
- Open DevTools → Network tab
- Look for API calls
- Check if they're going to the correct URL
- Look for 404 or CORS errors

### Blank Page After Deployment

**Check Build Output:**
- Go to Render logs
- Look for build errors
- Make sure `dist` folder was created

**Check Publish Directory:**
- Should be set to: `dist`
- Vite builds to `dist` by default

**Check Routes:**
If using React Router, you might need to add a `_redirects` file:

Create `frontend/public/_redirects`:
```
/*    /index.html   200
```

This ensures all routes work correctly.

---

## Important Configuration Files

### 1. frontend/vite.config.js
```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],
  build: {
    outDir: 'dist',
  },
})
```

### 2. frontend/.env.production
```
VITE_API_URL=https://feedback-backend-x85o.onrender.com
```

### 3. frontend/src/config.js
```javascript
const API_URL = import.meta.env.VITE_API_URL || 'https://feedback-backend-x85o.onrender.com';
export default API_URL;
```

---

## Post-Deployment Checklist

- [ ] Frontend loads successfully
- [ ] Can navigate between pages
- [ ] Signup works
- [ ] Login works
- [ ] Can submit feedback
- [ ] Admin dashboard loads (if applicable)
- [ ] No console errors
- [ ] API calls are successful
- [ ] Data persists in database

---

## Custom Domain (Optional)

### Add Custom Domain:
1. Go to your frontend service in Render
2. Click **"Settings"** → **"Custom Domains"**
3. Click **"Add Custom Domain"**
4. Enter your domain (e.g., `feedback.yourdomain.com`)
5. Follow DNS configuration instructions
6. Wait for SSL certificate to be issued

---

## Performance Optimization

### Enable Caching:
Render automatically caches static assets.

### CDN:
Render serves static sites via CDN automatically.

### Compression:
Vite automatically minifies and compresses your build.

---

## Monitoring

### Check Logs:
1. Go to your frontend service
2. Click **"Logs"** tab
3. Monitor for any issues

### Analytics (Optional):
Consider adding:
- Google Analytics
- Sentry for error tracking
- LogRocket for session replay

---

## Cost

**Free Tier:**
- Static sites are FREE on Render
- Unlimited bandwidth
- Automatic SSL
- CDN included

**No credit card required for static sites!**

---

## Quick Reference

**Build Command:**
```bash
npm install && npm run build
```

**Publish Directory:**
```
dist
```

**Environment Variables:**
```
VITE_API_URL=https://feedback-backend-x85o.onrender.com
```

**Root Directory:**
```
frontend
```

---

## Next Steps After Deployment

1. ✅ Test all features thoroughly
2. ✅ Set up custom domain (optional)
3. ✅ Add analytics (optional)
4. ✅ Set up error monitoring (optional)
5. ✅ Share your app with users! 🎉

---

## Your Deployed URLs

**Frontend:** `https://feedback-frontend-3mdn.onrender.com`
**Backend:** `https://feedback-backend-x85o.onrender.com`
**Database:** Connected via DATABASE_URL

---

## Need Help?

If you encounter issues:
1. Check Render build logs
2. Verify environment variables
3. Check browser console for errors
4. Verify backend is running
5. Test API endpoints directly

**Common Issues:**
- Build fails → Check package.json and build command
- Blank page → Check publish directory and build output
- API errors → Verify VITE_API_URL is set correctly
- CORS errors → Check backend CORS configuration

---

## 🎉 Ready to Deploy!

Follow the steps above and your frontend will be live in minutes!

Your complete app will be accessible at:
- **Frontend:** https://feedback-frontend-3mdn.onrender.com
- **Backend API:** https://feedback-backend-x85o.onrender.com

Good luck! 🚀
