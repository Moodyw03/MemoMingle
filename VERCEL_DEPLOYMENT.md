# Vercel Deployment Checklist

Use this checklist to ensure your My Cloud Diary application is ready for deployment on Vercel.

## Pre-Deployment Checks

### Code and Configuration

- [x] `app.py` has necessary imports and configurations
- [x] `app.py` has the `if __name__ == "__main__"` entry point
- [x] Flask-CORS is properly initialized
- [x] `vercel.json` is configured correctly
- [x] `requirements.txt` includes all necessary dependencies
- [ ] All local development-only code is commented out or removed
- [ ] Debug mode is turned off for production

### Environment Variables

- [ ] `.env` file is not committed to the repository (included in .gitignore)
- [ ] `.env.example` file is included with placeholders for required variables
- [ ] All required environment variables are documented in README.md

### Security

- [ ] No sensitive information (API keys, credentials) is hardcoded in the application
- [ ] Security headers are implemented
- [ ] Session management is configured properly
- [ ] CORS is properly configured

### Testing

- [ ] Application has been tested locally with all features
- [ ] Critical paths (authentication, note creation, etc.) have been verified

## Vercel Setup Steps

1. **Push your code to GitHub:**

   ```
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push origin main
   ```

2. **Login to Vercel:**

   - Go to [vercel.com](https://vercel.com)
   - Log in with your account or create a new one

3. **Create a new project:**

   - Click "New Project"
   - Import your GitHub repository
   - Configure the project settings:
     - Framework Preset: Other
     - Root Directory: ./
     - Build Command: (leave empty)
     - Output Directory: (leave empty)

4. **Configure environment variables:**

   - Add the following variables:
     - `SUPABASE_URL`: Your Supabase project URL
     - `SUPABASE_ANON_KEY`: Your Supabase anonymous key
     - `SECRET_KEY`: A secure random string for Flask sessions

5. **Deploy:**
   - Click "Deploy"
   - Wait for the deployment to complete
   - Test your deployed application

## Post-Deployment Checks

- [ ] Application loads correctly at the Vercel URL
- [ ] User registration works
- [ ] User login works
- [ ] Creating, editing, and deleting notes work
- [ ] Search functionality works
- [ ] No browser console errors

## Troubleshooting Common Issues

### Application Error (500)

- Check Vercel logs for detailed error information
- Verify all environment variables are set correctly
- Ensure all dependencies are properly listed in requirements.txt

### Static Files Not Loading

- Verify static file paths are correct
- Check that Flask is configured to serve static files correctly

### Database Connection Issues

- Verify Supabase credentials are correct
- Check that your IP is allowlisted in Supabase if necessary
- Verify database tables have been set up correctly

### CORS Errors

- Check CORS configuration in app.py
- Verify API endpoints are being called from allowed origins

## Useful Commands

**View Vercel logs:**

```
vercel logs your-project-name
```

**Pull environment variables to local development:**

```
vercel env pull
```

**Force a new deployment:**

```
vercel --force
```
