import {sqliteTable,text,integer,index} from 'drizzle-orm/sqlite-core';
export const savedItems=sqliteTable('saved_items',{
  id:text('id').primaryKey(),
  ownerId:text('owner_id').notNull(),
  kind:text('kind').notNull(),
  guideId:text('guide_id'),
  title:text('title').notNull(),
  data:text('data').notNull(),
  version:integer('version').notNull().default(1),
  createdAt:text('created_at').notNull(),
  updatedAt:text('updated_at').notNull()
},table=>[index('saved_items_owner_updated').on(table.ownerId,table.updatedAt)]);
