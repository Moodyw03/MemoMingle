# My Cloud Diary

## 🚨 Important Update: Now Using Supabase

This application has been migrated from MongoDB to Supabase for enhanced performance, reliability, and security. See [SUPABASE_MIGRATION.md](SUPABASE_MIGRATION.md) for details on the migration process.

<h1 align="center">My Cloud Diary</h1>

[View the live project here.](https://myclouddiary.vercel.app/)

Welcome to My Cloud Diary, an intuitive and secure note-taking application designed to streamline the way you capture and organize your thoughts. This application serves as a personal and professional aid, allowing users to create, edit, and manage notes with ease. The modern user interface, built with a focus on user experience, incorporates contemporary design principles to ensure that navigation and note management are both seamless and efficient.

Whether you're jotting down quick reminders or compiling detailed research notes, My Cloud Diary is your go-to solution for storing information securely. This document will guide you through every aspect of using My Cloud Diary, from initial setup to advanced features.

This submission represents Milestone Project 3 for the Code Institute's Diploma in Web Application Development program. The application utilizes HTML, CSS, JavaScript, and Python technologies along with Flask and Supabase to deliver a complete note-taking solution.

<div align="center">
<a href="https://ibb.co/T1yzLCd"><img src="https://i.ibb.co/hc0pfqw/memomingle-copy.jpg" alt="memomingle-copy" border="0"></a>
</div>

## Repository

[Find the project repository here:](https://github.com/Moodyw03/My-Cloud-Diary)

## User Experience (UX)

### User Stories

**As a New Visitor:**

- I want to quickly understand the purpose and benefits of My Cloud Diary so I can determine if it meets my needs
- I need intuitive navigation to explore the app's features
- I expect to find compelling reasons to register, such as enhanced productivity and secure note management
- I want to easily contact administrators with questions or feedback

**As a Registered User:**

- I need a simple and secure sign-in process to access my personal dashboard
- I want to create notes quickly and organize them with tags or categories
- I should be able to edit or delete my notes with changes reflected in real-time
- I expect robust search functionality to quickly find notes by keywords or tags
- I need a profile area to view my activity and update account details

**As a Frequent User:**

- I want advanced note-taking features to enhance my content
- I would appreciate access to version history for my notes
- I expect consistent performance and reliability

### UI Design Philosophy

My Cloud Diary's user interface is crafted with simplicity and ease of use as core principles. The UI employs a warm, pastel color palette that creates a welcoming environment, enhancing user concentration and reducing visual strain during note management tasks.

Key design elements include:

- **Minimalistic Layout:** Clean interface that avoids clutter, directing user focus
- **Intuitive Controls:** Commonly used actions are prominently placed and easily accessible
- **Consistent Visual Elements:** Familiar icons and consistent color coding for quick recognition
- **Responsive Design:** UI adjusts seamlessly across all devices, maintaining functionality and aesthetics

The design choices are informed by psychological principles that associate certain colors with memory and cognitive function, making the note-taking process effortless and pleasant.

<div align="center"><a href="https://ibb.co/FY9j5t5"><img src="https://i.ibb.co/vdbK383/memomingle-colors-copy.jpg" alt="memomingle-colors-copy" border="0"></a></div>

### Color Scheme

The color scheme is carefully selected to balance aesthetic appeal with functional design. Muted tones like 'Moon Mist' and 'Cape Cod' create a professional and minimalist interface, while warmer colors like 'Granite Green' and 'Crocodile' add subtle energy. Text colors like 'Shark' and 'Heavy Metal' provide excellent readability against lighter backgrounds, ensuring accessibility and reducing eye strain.

<div align="center"><a href="https://ibb.co/BVZPvB2"><img src="https://i.ibb.co/4ZTfCpR/color-scheme-memomingle-copy.jpg" alt="color-scheme-memomingle-copy" border="0"></a></div>

### Typography

My Cloud Diary employs 'Inter' as the primary typeface—a highly legible sans-serif font crafted for digital screens that ensures readability at various sizes. The clean lines and open shapes contribute to the modern feel of the interface. As fallbacks, 'Arial' and generic 'sans-serif' fonts maintain design integrity across different environments, providing a seamless reading experience aligned with the app's user-centric design principles.

### Wireframes

Home Page Wireframe - [View](https://pdfhost.io/v/sJqhKgCY7_MemoMingle_Wireframes)

## Code Architecture

### App Structure

- **config/**: Configuration files including db.py for database connections
- **controllers/**: Contains auth_controller.py and note_controller.py for handling authentication and note operations
- **models/**: Includes user.py and note.py defining data models
- **static/**: Stores CSS, JS, and images for the frontend
- **templates/**: Contains HTML templates for rendering views
- **app.py**: Main entry point of the Flask application
- **.env**: Stores environment variables (not included in version control)

### Database Schema

- **Users Table**: Stores username, email, and securely hashed passwords
- **Notes Table**: Stores notes with fields for title, content, tags, creation and modification timestamps

### API Endpoints

- **Authentication**: `/auth/sign-in`, `/auth/sign-up`, `/auth/sign-out` for user authentication flow
- **Note Management**: `/notes/`, `/notes/new`, `/notes/<id>/delete`, `/notes/<id>/edit` for CRUD operations

<div align="center"><a href="https://ibb.co/vvSkVMb"><img src="https://i.ibb.co/yBrqdxD/flowchart.jpg" alt="flowchart" border="0"></a></div>

## Core Functionality

<div align="center"><a href="https://ibb.co/DMP8830"><img src="https://i.ibb.co/X5f33mc/crud1.jpg" alt="crud1" border="0"></a></div>

## Features

### Authentication System

- **Secure Sign-Up**: Users register with username and password; passwords are securely hashed before storage
- **Sign-In**: Credentials are validated against stored hashed passwords with session management
- **Sign-Out**: Sessions are properly terminated for security

### Note Management

- **Creating Notes**: Users can create notes with title, content, and optional tags
- **Updating Notes**: Existing notes can be modified with changes saved in real-time
- **Deleting Notes**: Users can remove notes with confirmation to prevent accidental deletion
- **Searching Notes**: Comprehensive search across note titles, content, and tags

### Error Handling

- **User Feedback**: Clear error messages and success notifications
- **Validation**: Input validation with helpful prompts for correction
- **Graceful Error Recovery**: System maintains stability during unexpected conditions

## Security Features

Security is a top priority in My Cloud Diary:

- **Password Security**: Werkzeug's security module for password hashing
- **Session Management**: Flask-Session for secure, server-side session handling
- **Environment Protection**: Sensitive information stored in environment variables
- **HTTPS Enforcement**: Secure data transmission between client and server
- **Input Validation**: Thorough validation to prevent injection attacks

For more detailed security information, please see our [SECURITY.md](SECURITY.md) file.

## Testing

For comprehensive testing information, [view our testing documentation](testing.md).

## Recent Improvements

We've addressed several key issues to enhance user experience:

- **Enhanced Authentication**: Implemented mandatory password validation with minimum character requirements
- **Improved Error Feedback**: Refined error handling for clearer user communication
- **Data Protection**: Added confirmation dialogs for irreversible actions like note deletion
- **Search Enhancement**: Optimized search to include tags, titles, and descriptions for better results
- **UI Consistency**: Updated footer design to match navbar for visual coherence

## Deployment

### Live Version

Experience My Cloud Diary in action on our [live site](https://myclouddiary.vercel.app/).

### Local Development Setup

To run My Cloud Diary locally:

1. **Clone the repository**:

   ```
   git clone https://github.com/Moodyw03/My-Cloud-Diary.git
   ```

2. **Set up the environment**:

   ```
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:

   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file based on `.env.example` with your Supabase credentials.

5. **Run the application**:
   ```
   export FLASK_APP=app
   export FLASK_ENV=development
   flask run
   ```
   On Windows Command Prompt:
   ```
   set FLASK_APP=app
   set FLASK_ENV=development
   flask run
   ```
   Or PowerShell:
   ```
   $env:FLASK_APP="app"
   $env:FLASK_ENV="development"
   flask run
   ```

### Production Deployment

For production deployment on Vercel:

1. **Prepare your GitHub repository:**

   - Ensure your code is pushed to GitHub
   - Make sure all dependencies are listed in requirements.txt
   - Verify vercel.json configuration is in the root directory

2. **Set up Vercel deployment:**

   - Create a Vercel account at [vercel.com](https://vercel.com)
   - From the Vercel dashboard, click "New Project"
   - Import your GitHub repository
   - Configure the project:
     - Framework Preset: Other
     - Build Command: Leave empty (uses vercel.json)
     - Output Directory: Leave empty (uses vercel.json)

3. **Configure environment variables:**

   - In the Vercel project settings, navigate to "Environment Variables"
   - Add the following variables:
     - `SUPABASE_URL`: Your Supabase project URL
     - `SUPABASE_ANON_KEY`: Your Supabase anonymous key
     - `SECRET_KEY`: A secure random string for Flask sessions

4. **Deploy your application:**

   - Click "Deploy" to start the deployment process
   - Vercel will build and deploy your application automatically
   - Once complete, your application will be available at your Vercel URL

5. **Configure custom domain (optional):**
   - In the Vercel project settings, navigate to "Domains"
   - Add your custom domain and follow the instructions for DNS setup

Vercel will automatically redeploy your application whenever you push changes to your GitHub repository's main branch.

## Technologies Used

My Cloud Diary leverages the following technologies:

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask framework
- **Database**: Supabase (PostgreSQL)
- **Authentication**: Flask-Session, Werkzeug security
- **Deployment**: Vercel
- **Version Control**: Git, GitHub
- **Development Tools**: Visual Studio Code, ESLint
- **Design Tools**: Eraser for wireframes and flowcharts

## Credits

- Images created with DALL-E
- Icons from FontAwesome and Lucide

## Acknowledgements

I am deeply appreciative of:

- Fellow students and alumni of the Code Institute for their support
- Manu Perez and Pasquale for their mentorship at Bristol College
- Tutors and staff at the Code Institute for their guidance
- The Code Institute London Community for their encouragement
- My family for their patience and understanding during this project

Gabriel Pereira, 2024.

## Content

All content was written by the developer.
