# Deploy to GitHub Pages

## Step 1: Build the Static Site

Run the build command to generate the static export:

```bash
npm run build
```

This creates an `out/` directory with all static files.

## Step 2: Add .nojekyll File

Create an empty `.nojekyll` file in the `out/` directory:

```bash
New-Item -Path out/.nojekyll -ItemType File
```

This tells GitHub Pages not to process files with Jekyll.

## Step 3: Push to GitHub

1. Make sure all changes are committed:
```bash
git add .
git commit -m "Initial Istaris landing page"
git push origin main
```

2. Push the `out/` directory to a `gh-pages` branch:
```bash
git subtree push --prefix out origin gh-pages
```

Or use this PowerShell script for easier deployment:
```powershell
# Build the site
npm run build

# Add .nojekyll file
New-Item -Path out/.nojekyll -ItemType File -Force

# Deploy to gh-pages branch
git add -f out
git commit -m "Deploy to GitHub Pages"
git subtree push --prefix out origin gh-pages
```

## Step 4: Configure GitHub Pages

1. Go to your repository on GitHub: `https://github.com/YOUR_USERNAME/istaris`
2. Click on **Settings**
3. Scroll to **Pages** in the left sidebar
4. Under **Source**, select `gh-pages` branch
5. Click **Save**

## Step 5: Access Your Site

Your site will be available at:
```
https://YOUR_USERNAME.github.io/istaris/
```

## Updating the Site

Whenever you make changes:

```bash
npm run build
New-Item -Path out/.nojekyll -ItemType File -Force
git add -f out
git commit -m "Update site"
git subtree push --prefix out origin gh-pages
```

## Alternative: GitHub Actions (Recommended)

For automatic deployment, you can set up GitHub Actions. Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        
    - name: Install dependencies
      run: npm ci
      
    - name: Build
      run: npm run build
      
    - name: Add .nojekyll
      run: touch out/.nojekyll
      
    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./out
```

With this setup, your site will automatically deploy whenever you push to the main branch!
