import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwindcss from '@tailwindcss/vite';
import { unified } from '@astrojs/markdown-remark';
import rehypeExternalLinks from 'rehype-external-links';

export default defineConfig({
  integrations: [react()],
  vite: {
    plugins: [tailwindcss()],
  },
  markdown: {
    processor: unified({
      rehypePlugins: [
        [rehypeExternalLinks, { target: '_blank', rel: ['noopener', 'noreferrer'] }],
      ],
    }),
  },
});
