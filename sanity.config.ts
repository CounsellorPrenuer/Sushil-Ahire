import { defineConfig } from 'sanity';
import { structureTool } from 'sanity/structure';
import { schema } from './src/sanity/schemas';

export default defineConfig({
  basePath: '/studio',
  projectId: '7secz1ar',
  dataset: 'production',
  title: 'Future Map - Dr Sushil Ahire',

  plugins: [structureTool()],

  schema: {
    types: schema,
  },
});
