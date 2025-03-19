# Simple Django CRUD App

A simple Create, Read, Update, and Delete (CRUD) application built using Django. This app allows users to manage data efficiently with basic authentication and a user-friendly interface.

## Features

- User authentication (login/logout)
- CRUD operations for managing records
- Search functionality
- Responsive UI with Bootstrap

## Installation

### Prerequisites
Ensure you have the following installed:

- Python (>=3.8)
- Django (>=4.0)
- SQLite (default database) or PostgreSQL/MySQL (optional)

### Setup Steps

1. **Clone the repository**
   ```sh
   git clone https://github.com/harsh-sharawat/crud_django.git
   cd crm  
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser** (optional for admin access)
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```sh
   python manage.py runserver
   ```

7. Open your browser and go to:
   ```sh
   http://127.0.0.1:8000/
   ```

## Usage
- Login to the system.
- Add new records.
- Edit or delete existing records.
- Manage data efficiently.

