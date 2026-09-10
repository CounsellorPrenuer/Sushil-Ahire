export default {
  name: 'founder',
  title: 'Founder Info',
  type: 'document',
  fields: [
    {
      name: 'name',
      title: 'Name',
      type: 'string',
    },
    {
      name: 'title',
      title: 'Title',
      type: 'string',
    },
    {
      name: 'photo',
      title: 'Photo',
      type: 'image',
      options: { hotspot: true },
    },
    {
      name: 'biography',
      title: 'Biography',
      type: 'array',
      of: [{ type: 'block' }],
    },
    {
      name: 'experience',
      title: 'Experience',
      type: 'text',
    },
    {
      name: 'achievements',
      title: 'Achievements',
      type: 'array',
      of: [{ type: 'string' }],
    },
    {
      name: 'philosophy',
      title: 'Philosophy',
      type: 'text',
    },
  ],
};
