# Frontend Deployment Checklist

## Quick Deployment Steps

### Before You Start
- [ ] Backend is live: https://feedback-backend-x85o.onrender.com
- [ ] Code is pushed to GitHub
- [ ] You're logged into Render

---

## Deployment Steps (5 minutes)

### Step 1: Create Static Site
- [ ] Go to https://dashboard.render.com
- [ ] Click "New +" → "Static Site"
- [ ] Connect repository: `Abhijith-PA1/Feedback`

### Step 2: Configure Settings

**Basic Info:**
- [ ] Name: `feedback-frontend`
- [ ] Region: Oregon (US West)
- [ ] Branch: `main`
- [ ] Root Directory: `frontend`

**Build Settings:**
- [ ] Build Command:
  ```
  npm install && npm run build
  ```

- [ ] Publish Directory:
  ```
  dist
  ```

**Environment Variables:**
- [ ] Add: `VITE_API_URL` = `https://feedback-backend-x85o.onrender.com`

### Step 3: Deploy
- [ ] Click "Create Static Site"
- [ ] Wait 2-3 minutes for build
- [ ] Check logs for errors

---

## Verification (2 minutes)

- [ ] Frontend loads: `https://feedback-frontend.onrender.com`
- [ ] Can navigate between pages
- [ ] Signup works
- [ ] Login works
- [ ] Can submit feedback
- [ ] No console errors (F12 → Console)

---

## If Something Goes Wrong

### Build Fails?
→ Check Root Directory is set to `frontend`
→ Verify Build Command is correct

### Blank Page?
→ Check Publish Directory is `dist`
→ Check browser console for errors

### API Calls Fail?
→ Verify VITE_API_URL environment variable
→ Check backend is running
→ Check browser Network tab (F12)

---

## Done! 🎉

Your app is now fully deployed:
- **Frontend:** https://feedback-frontend.onrender.com
- **Backend:** https://feedback-backend-x85o.onrender.com

Test it and share with users! 🚀

---

## Important Files Created

- ✅ `frontend/public/_redirects` - For React Router support
- ✅ `render.yaml` - Updated with frontend config
- ✅ `FRONTEND_DEPLOYMENT_GUIDE.md` - Detailed guide

All changes are ready to commit and push!
