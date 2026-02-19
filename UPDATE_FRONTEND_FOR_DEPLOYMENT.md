# 🔧 Update Frontend for Deployment

Quick guide to update all API calls in your frontend to use the backend URL.

---

## Step 1: Update Each Page File

You need to update 4 files to use the API_URL from config.

### File 1: `frontend/src/pages/Signup.jsx`

**Add import at top:**
```javascript
import API_URL from '../config'
```

**Update axios call (line ~30):**
```javascript
// Change from:
const res = await axios.post('/api/auth/signup', formData)

// To:
const res = await axios.post(`${API_URL}/api/auth/signup`, formData)
```

---

### File 2: `frontend/src/pages/Login.jsx`

**Add import at top:**
```javascript
import API_URL from '../config'
```

**Update axios call:**
```javascript
// Change from:
const res = await axios.post('/api/auth/login', formData)

// To:
const res = await axios.post(`${API_URL}/api/auth/login`, formData)
```

---

### File 3: `frontend/src/pages/Feedback.jsx`

**Add import at top:**
```javascript
import API_URL from '../config'
```

**Update axios call:**
```javascript
// Change from:
const res = await axios.post('/api/feedback', feedbackData, {

// To:
const res = await axios.post(`${API_URL}/api/feedback`, feedbackData, {
```

---

### File 4: `frontend/src/pages/AdminDashboard.jsx`

**Add import at top:**
```javascript
import API_URL from '../config'
```

**Update axios call:**
```javascript
// Change from:
const res = await axios.get('/api/admin/dashboard', {

// To:
const res = await axios.get(`${API_URL}/api/admin/dashboard`, {
```

---

## Step 2: Test Locally

After making changes, test locally:

```bash
cd frontend
npm run dev
```

Should still work with `http://localhost:5000`

---

## Step 3: Deploy

Once tested, commit and push:

```bash
git add .
git commit -m "Update API calls for deployment"
git push origin main
```

Render will automatically deploy the changes!

---

## Alternative: Automated Script

If you want, I can create a script to automatically update all files. Let me know!
