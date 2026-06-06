# AlgoAtlas — Learning Website

Built with [Astro](https://astro.build) · Tailwind CSS · React · Mermaid.js

## Features

- 22 DSA pattern pages with diagrams and problem tables
- Mermaid mindmaps and flowcharts rendered client-side
- LeetCode-linked problem tables with difficulty badges
- Syntax-highlighted Python solutions (Shiki, github-dark theme)
- Interactive step-through visualizers: Sliding Window, Two Pointers, BFS, Binary Search
- Pattern search on homepage

## Run locally

```bash
cd website/
npm install
npm run dev      # syncs content + starts dev server at localhost:4321
```

## Build

```bash
npm run build    # syncs content + builds static site to dist/
npm run preview  # preview the built site
```

## Deploy to Vercel

1. Push this repo to GitHub
2. Go to [vercel.com](https://vercel.com) → New Project → Import the repo
3. Set **Root Directory** to `website`
4. Vercel auto-detects Astro — deploy

Or via CLI from the `website/` directory:
```bash
npx vercel --prod
```

## How content works

The `scripts/sync-content.js` pre-build script copies `README.md`, `NOTES.md`, and `code/*/solution.py` from the parent DSA repo into `src/data/patterns/<slug>/` before Astro builds. This means:

- Edit the DSA patterns in the parent repo as normal
- Run `npm run dev` or `npm run build` — changes are picked up automatically
- The generated `src/content/patterns/` and `src/data/patterns/` directories are git-ignored
