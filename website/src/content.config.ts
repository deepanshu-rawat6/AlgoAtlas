import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const patterns = defineCollection({
  loader: glob({ pattern: '*.json', base: './src/content/patterns' }),
  schema: z.object({
    slug: z.string(),
    title: z.string(),
    phase: z.number(),
    problemCount: z.number(),
  }),
});

export const collections = { patterns };
