export default {
  name: 'mentoriaPackage',
  title: 'Mentoria Packages',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Package Title',
      type: 'string',
    },
    {
      name: 'image',
      title: 'Package Image',
      type: 'image',
      options: { hotspot: true },
    },
    {
      name: 'description',
      title: 'Description',
      type: 'text',
    },
    {
      name: 'price',
      title: 'Price',
      type: 'string',
    },
    {
      name: 'duration',
      title: 'Duration',
      type: 'string',
    },
    {
      name: 'sessions',
      title: 'Number of Sessions',
      type: 'string',
    },
    {
      name: 'features',
      title: 'Features',
      type: 'array',
      of: [{ type: 'string' }],
    },
    {
      name: 'featured',
      title: 'Is Featured?',
      type: 'boolean',
      initialValue: false,
    },
    {
      name: 'order',
      title: 'Order',
      type: 'number',
    },
  ],
  orderings: [
    {
      title: 'Manual Order',
      name: 'manualOrder',
      by: [{ field: 'order', direction: 'asc' }],
    },
  ],
};
