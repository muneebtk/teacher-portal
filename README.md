# Project Overview

This project implements a student management system using Django for the backend and vanilla JavaScript for the frontend. The project includes functionalities for managing students, user authentication, and dynamic interaction with the frontend.

## Features Implemented

### Backend

1. **Student CRUD Operations**:

   * Create, Read, Update, and Delete students.
2. **User Authentication**:

   * Login and Logout functionality.
   * Secure access to pages using Django's session-based authentication.
3. **Custom API Endpoints**:

   * `students/`: Fetch all students.
   * `students/<id>/`: Fetch, update, or delete a specific student.

### Frontend

1. **Dynamic Student Table**:

   * Rendered using DataTables for pagination and search.
2. **Popups**:

   * Popup forms for creating or editing student details.
   * Form validations for required fields.
3. **Reusable Components**:

   * A common navbar.
   * Success and error message notifications.
4. **Signup Page**:

   * Includes fields for first name, last name, email, password, and confirm password.
   * Validations for required fields and password match.

## Running the Project

### Prerequisites

* Python 3.x
* Django 4.x
* Node.js and npm (for frontend dependency installation, if required)
* A web browser

### Backend Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate  # For Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin user.
6. Run the development server:

   ```bash
   python manage.py runserver
   ```

### Frontend Setup

The frontend uses vanilla JavaScript and CSS. There are no additional setup steps required for the frontend.

### Running the Application

1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. Log in using the superuser credentials created earlier.
3. Access the student management system and other functionalities.

## Development Notes

* Use the Django admin panel (`/admin`) for debugging database entries.
* Ensure CSRF tokens are included in all POST requests to the backend.
* Update `settings.py` for any environment-specific configurations.



