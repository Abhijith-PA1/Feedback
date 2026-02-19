# Fix Render Deployment Error

## The Problem
Render can't find `requirements.txt` because it's looking in the root directory, but the file is in the `backend` folder.

## Solution: Update Render Dashboard Settings

### Option 1: Use render.yaml (Recommended)
1. Go to your Render Dashboard
2. Click on your service (feedback-api)
3. Go to **Settings** tab
4. Scroll to **Build & Deploy** section
5. Look for **"Root Directory"** field
6. Set it to: `backend`
7. Click **Save Changes**
8. Trigger a manual deploy

### Option 2: Update Build Command in Dashboard
If Option 1 doesn't work, update the build command:

1. Go to your Render Dashboard
2. Click on your service (feedback-api)
3. Go to **Settings** tab
4. Find **Build Command** field
5. Change it to:
   ```
   cd backend && pip install -r requirements.txt && python ml_model/train_emotion_model.py
   ```
6. Find **Start Command** field
7. Change it to:
   ```
   cd backend && gunicorn wsgi:app
   ```
8. Click **Save Changes**
9. Trigger a manual deploy

### Option 3: Create New Service from render.yaml
1. Delete the current service in Render
2. Create a new service
3. When asked, select **"Use render.yaml"**
4. Render will automatically configure everything from the `render.yaml` file in your repo

## Verify the Fix
After making changes, check the deployment logs. You should see:
- ✅ "Successfully installed flask flask-cors..."
- ✅ No more "Could not open requirements file" error

## Current Configuration
Your `render.yaml` is correctly configured with:
- `rootDir: backend` - tells Render where your code is
- Proper build and start commands
- All environment variables
