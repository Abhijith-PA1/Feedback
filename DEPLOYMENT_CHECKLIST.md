# ✅ Render Deployment Checklist

Quick checklist to deploy your app to Render.

---

## 📋 Pre-Deployment

- [ ] Code is in GitHub repository
- [ ] `EmotionDetection.csv` is in repository root
- [ ] Backend has `requirements.txt` with gunicorn
- [ ] Backend has `wsgi.py` file
- [ ] Frontend API calls updated (see UPDATE_FRONTEND_FOR_DEPLOYMENT.md)
- [ ] Render account created

---

## 🔧 Backend Deployment

- [ ] Create new Web Service on Render
- [ ] Connect GitHub repository
- [ ] Set root directory to `backend`
- [ ] Set build command: `pip install -r requirements.txt && python ml_model/train_emotion_model.py`
- [ ] Set start command: `gunicorn -c gunicorn_config.py wsgi:app`
- [ ] Add environment variables:
  - [ ] `PYTHON_VERSION` = `3.11.0`
  - [ ] `SECRET_KEY` = [Generate]
  - [ ] `JWT_SECRET_KEY` = [Generate]
- [ ] Deploy and wait (5-10 minutes)
- [ ] Copy backend URL: `https://feedback-api-xxxx.onrender.com`
- [ ] Test API: `curl https://your-url.onrender.com/api/auth/login`

---

## 🎨 Frontend Deployment

- [ ] Update `frontend/.env.production` with backend URL
- [ ] Create new Static Site on Render
- [ ] Connect GitHub repository
- [ ] Set root directory to `frontend`
- [ ] Set build command: `npm install && npm run build`
- [ ] Set publish directory: `dist`
- [ ] Add environment variable:
  - [ ] `VITE_API_URL` = `https://your-backend-url.onrender.com`
- [ ] Deploy and wait (2-3 minutes)
- [ ] Copy frontend URL: `https://feedback-frontend-xxxx.onrender.com`

---

## 🔐 CORS Configuration

- [ ] Update `backend/app.py` CORS settings with frontend URL
- [ ] Commit and push changes
- [ ] Wait for auto-deploy

---

## ✅ Testing

- [ ] Visit frontend URL
- [ ] Test signup (create new account)
- [ ] Test login (use created account)
- [ ] Submit feedback
- [ ] Login as admin (admin@gmail.com / admin123)
- [ ] Check admin dashboard
- [ ] Verify sentiment analysis works

---

## 🎉 Done!

Your app is live! Share the URL and celebrate! 🎊

**Frontend:** https://feedback-frontend-xxxx.onrender.com  
**Backend:** https://feedback-api-xxxx.onrender.com

---

## 📝 Notes

**Free Tier Limitations:**
- Backend sleeps after 15 min inactivity
- First request after sleep takes 10-30 seconds (cold start)
- Database resets on deploy (use PostgreSQL for persistence)

**For Production:**
- Upgrade to Starter plan ($7/month) for always-on backend
- Use PostgreSQL database ($7/month) for data persistence
- Add custom domain (optional)

---

**Need help?** Check `RENDER_DEPLOYMENT_GUIDE.md` for detailed instructions!
