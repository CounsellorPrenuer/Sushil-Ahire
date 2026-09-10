import { createClient } from 'next-sanity'

export const projectId = '7secz1ar'
export const dataset = 'production'
export const apiVersion = '2023-05-03'

export const client = createClient({
  projectId,
  dataset,
  apiVersion,
  useCdn: false, // Set to false for live updates
})
