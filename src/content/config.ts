import { defineCollection, z } from 'astro:content';

const models = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    image: z.string(),
    stl_path: z.string(),
    threemf_path: z.string().optional(),
    license: z.string(),
    author: z.string(),
    source_url: z.string().url(),
    difficulty: z.enum(['beginner', 'intermediate']),
    est_print_time_minutes: z.number().int(),
    supports_required: z.boolean(),
    layer_height_mm: z.number(),
    slicer_settings: z.record(z.string(), z.union([z.string(), z.number()])).optional(),
    description: z.string(),
    steps: z.array(z.string()).optional(),
    skill_tags: z.array(z.string()).optional(),
    featured: z.boolean().optional(),
  }),
});

const guides = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    order: z.number().int().min(1).max(8),
    est_read_time_minutes: z.number().int(),
    callout: z.string().optional(),
  }),
});

const glossary = defineCollection({
  type: 'content',
  schema: z.object({
    term: z.string(),
    definition: z.string(),
    image: z.string().optional(),
    see_also: z.array(z.string()).optional(),
    gotcha: z.string().optional(),
  }),
});

export const collections = { models, guides, glossary };
