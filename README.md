# Istaris

AI-powered digital employees that work 24/7 to automate your entire workflow.

## 🚀 Project Overview

Istaris is an AI automation company landing page built with Next.js, featuring a bold "Stop Hiring Humans" message inspired by Artisan's approach. The site showcases digital employees that can automate roles like Scrum Masters and Digital Marketing Specialists.

## ✨ Features

- **Modern Design**: Dark theme with vibrant gradient accents
- **Responsive**: Fully responsive across all devices
- **Animations**: Smooth fade-in and hover effects
- **Static Export**: Optimized for GitHub Pages deployment
- **SEO Optimized**: Meta tags and semantic HTML

## 🛠️ Tech Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: CSS Modules with custom design system
- **Deployment**: GitHub Pages

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/istaris.git

# Navigate to the directory
cd istaris

# Install dependencies
npm install

# Run development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the site.

## 🏗️ Build

```bash
# Build for production
npm run build
```

This generates a static export in the `out/` directory.

## 🚀 Deployment

See [DEPLOY.md](./DEPLOY.md) for detailed GitHub Pages deployment instructions.

Quick deploy:
```bash
npm run build
New-Item -Path out/.nojekyll -ItemType File -Force
git subtree push --prefix out origin gh-pages
```

## 📁 Project Structure

```
istaris/
├── app/
│   ├── components/
│   │   ├── Hero.tsx        # Hero section with "Stop Hiring Humans"
│   │   ├── Features.tsx    # Features grid
│   │   ├── Benefits.tsx    # Benefits with stats
│   │   └── CTA.tsx         # Call-to-action section
│   ├── globals.css         # Design system and global styles
│   ├── layout.tsx          # Root layout with SEO
│   └── page.tsx            # Main landing page
├── .github/
│   └── workflows/
│       └── deploy.yml      # Automated GitHub Pages deployment
└── next.config.mjs         # Next.js configuration for static export
```

## 🎨 Design System

The design system features:
- Dark background with vibrant purple/pink gradients
- Inter font family from Google Fonts
- Custom CSS properties for consistency
- Glassmorphism effects
- Smooth animations and transitions

## 📄 License

See [LICENSE](./LICENSE) file for details.

## 🤝 Contributing

This is a company landing page project. For major changes, please open an issue first.

---

Built with ❤️ for the future of work
