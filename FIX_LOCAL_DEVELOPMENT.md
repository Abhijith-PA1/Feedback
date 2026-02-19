# Fix Local Development - Proxy Error

## Problem
When running `npm run dev` locally, you get:
```
[vite] http proxy error: /api/auth/login
```

This happens because Vite's proxy is trying to connect to `localhost:5000`, but your backend is not running locally.

## Solution

### Option 1: Use Live Backend (Recommended)

I've created `.env.local` file that tells your local frontend to use the live backend:

**File: `frontend/.env.local`**
```
VITE_API_URL=https://feedback-backend-x85o.onrender.com
```

**Steps:**
1. Stop your dev server (CTRL+C)
2. Restart it:
   ```bash
   cd frontend
   npm run dev
   ```
3. The frontend will now use the live backend ✅

### Option 2: Run Backend Locally

If you want to run the backend locally:

**Step 1: Start Backend**
```bash
cd backend
python app.py
```

**Step 2: Update vite.config.js**
Uncomment the proxy section:
```javascript
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
      },
    },
  },
})
```

**Step 3: Delete .env.local**
```bash
rm frontend/.env.local
```

**Step 4: Restart Frontend**
```bash
cd frontend
npm run dev
```

## Current Configuration

### For Local Development (using live backend)
- ✅ `.env.local` created with live backend URL
- ✅ Proxy disabled in `vite.config.js`
- ✅ Frontend connects directly to: `https://feedback-backend-x85o.onrender.com`

### For Production (deployed)
- ✅ `.env.production` has live backend URL
- ✅ Works automatically when deployed

## How It Works

Vite loads environment variables in this order:
1. `.env.local` (local development - highest priority)
2. `.env.production` (production builds)
3. `.env` (default fallback)

Your `config.js` uses:
```javascript
const API_URL = import.meta.env.VITE_API_URL || 'https://feedback-backend-x85o.onrender.com';
```

## Restart Your Dev Server

```bash
# Stop current server (CTRL+C)
cd frontend
npm run dev
```

The error should be gone! ✅

## Verify It's Working

1. Open: http://localhost:5173 (or your dev server URL)
2. Open browser console (F12)
3. Try to log in
4. Check Network tab - should see calls to `https://feedback-backend-x85o.onrender.com`
5. No more proxy errors! ✅

## Important Notes

**`.env.local` is gitignored** - This is correct! Each developer can have their own local configuration.

**For team development:**
- Some developers might run backend locally
- Others might use the live backend
- Each can configure their own `.env.local`

## Troubleshooting

### Still Getting Proxy Error?
1. Make sure you restarted the dev server
2. Check `.env.local` exists in `frontend/` folder
3. Clear browser cache
4. Try hard refresh (CTRL+SHIFT+R)

### API Calls Not Working?
1. Check browser console for errors
2. Verify backend is running: https://feedback-backend-x85o.onrender.com/api/auth/login
3. Check CORS settings in backend
4. Verify VITE_API_URL is loaded (console.log it in config.js)

### Backend Spinning Down?
- Free tier spins down after 15 minutes
- First request takes 30-60 seconds
- Subsequent requests are fast
- Consider upgrading for production

---

## Quick Fix Summary

1. ✅ Created `.env.local` with live backend URL
2. ✅ Disabled proxy in `vite.config.js`
3. ✅ Restart dev server: `npm run dev`
4. ✅ Error fixed!

Your local development now uses the live backend, so you don't need to run the backend locally! 🚀
