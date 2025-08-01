# Django Login System

This is a simple and extensible Django-based login and authentication system. It includes views, templates, and static CSS for home, login, and signup pages.

## Features

- User Sign-Up & Login
- Authentication using Django’s built-in user model
- Static CSS styling for clean UI
- Easily extendable for profile or dashboard functionality

---

## 🔧 Installation

### 1. Clone the repo
```bash
git clone https://github.com/harmansingh2005/LoginSystem
```
### 2. Create Virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run migrations
```bash
python manage.py migrate
```
### 5. Start the development server
```bash
python manage.py runserver
```

## How To Access the App

Once the development server is running, visit the following in your browser:
- Home Page: ***http://127.0.0.1:8000/***
- Login: ***http://127.0.0.1:8000/login/***
- Sign-Up: ***http://127.0.0.1:8000/signup/***

> Make sure your *urls.py* is correctly routing these views.
