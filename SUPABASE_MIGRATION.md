# MongoDB to Supabase Migration Guide for My Cloud Diary

This document provides instructions for migrating your note-taking application from MongoDB to Supabase.

## Steps to Complete Migration

### 1. Sign Up for Supabase

1. Go to [Supabase](https://supabase.com/) and create a new account or sign in.
2. Create a new project and note down your Supabase URL and anon key.

### 2. Set Up Database Schema

1. In your Supabase project, go to the SQL Editor.
2. Run the SQL schema provided in `schema.sql` to create the necessary tables and policies.

### 3. Update Environment Variables

Update your `.env` file with your Supabase credentials:

```
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_supabase_anon_key
SECRET_KEY=your_secret_key
```

Also update these in your Vercel environment variables.

### 4. Install Supabase Client Library

```bash
pip install supabase
```

### 5. Import Data (Optional)

If you need to import existing data from MongoDB to Supabase:

1. Export your MongoDB data:

   ```bash
   mongoexport --uri="your_mongo_uri" --collection=users --out=users.json
   mongoexport --uri="your_mongo_uri" --collection=notes --out=notes.json
   ```

2. Transform the data format to match Supabase schema (you may need to write a conversion script).

3. Import into Supabase using the SQL Editor or Supabase client.

## Changes Made During Migration

1. **Authentication System**: Updated to use Supabase's PostgreSQL database while maintaining the existing authentication flow.

2. **Data Models**: Converted from MongoDB documents to PostgreSQL relational tables.

3. **Search Functionality**: Updated to use PostgreSQL's text search capabilities instead of MongoDB's regex search.

4. **ID Handling**: Changed from MongoDB's ObjectId to UUID format.

## Troubleshooting

- **Authentication Issues**: Ensure passwords are properly hashed in the Supabase users table.
- **Data Type Inconsistencies**: Check that date fields are properly formatted as ISO strings.
- **Missing Data**: If any data appears missing, verify the import process was complete.

## Benefits of Supabase

- Built-in authentication and authorization
- Real-time capabilities
- SQL-based queries for more complex data operations
- Simpler scalability
- Built-in row-level security for better data protection
