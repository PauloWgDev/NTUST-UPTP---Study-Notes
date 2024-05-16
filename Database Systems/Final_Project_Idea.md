

### Project Overview

**Objective:** Develop a Flashcards app in Android Studio using RoomDB to manage flashcards, categories, and user progress.

### Key Features

1. **User Management:**
    
    - Profile creation and management.
    - Tracking user progress and statistics.
2. **Flashcard Management:**
    
    - CRUD operations for flashcards.
    - Organize flashcards into Groups.
    - Tagging for flashcards.
3. **Study Sessions:**
    - Start a study session with selected flashcards or categories.
    - Track correct and incorrect responses.
    - Provide feedback on performance.
4. **Statistics and Progress Tracking:**
    
    - Track study sessions, number of correct/incorrect responses.
    - Display progress over time.
5. **Search and Filter:**
    
    - Search flashcards by keywords, tags, categories.
    - Filter flashcards based on user performance (e.g., least known cards).
### Database Schema

Here’s a basic schema to get you started:

1. **Users Table:**
    
    - `user_id` (Primary Key)
    - `username`
    - `password_hash`
    - `email`
    - `created_at`
2. ==Groups Table:**== 
    
    - `group_id` (Primary Key)
    - `group_name`
    - `description`
3. ==**Flashcards Table:** (Done)==
    
    - `flashcard_id` (Primary Key)
    - `question`
    - `answer`
    - `category_id` (Foreign Key)
    - `user_id` (Foreign Key, to indicate the creator)
4. **Tags Table:**
    
    - `tag_id` (Primary Key)
    - `tag_name`
5. **FlashcardTags Table:**
    
    - `flashcard_id` (Foreign Key)
    - `tag_id` (Foreign Key)
6. **StudySessions Table:**
    
    - `session_id` (Primary Key)
    - `user_id` (Foreign Key)
    - `started_at`
    - `ended_at`
7. **SessionDetails Table:**
    
    - `session_id` (Foreign Key)
    - `flashcard_id` (Foreign Key)
    - `is_correct` (Boolean)

### Additional Features (Optional)

- **Spaced Repetition System (SRS):** Implement an algorithm to optimize the review intervals based on user performance.
- **Import/Export:** Allow users to import/export flashcards in various formats (e.g., CSV, JSON). (Basic Version Done)
