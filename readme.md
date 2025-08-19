# alx_travel_app_0x01

This is a Django RESTful application for managing travel listings, bookings, and reviews.

## Project Overview

This project is part of ALX Software Engineering program.

## Project Structure

- `listings/` — Django app containing models, serializers, and seed logic
- `alx_travel_app/` — Main project settings and URL configuration
- `requirements.txt` — Python dependencies
- `README.md` — Project setup and documentation

## Features

- Create and view travel listings
- Book available listings by date
- Leave reviews on listings

## Technologies Used

- Python 3
- Django 3.2
- Django REST Framework

## Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/Stev1000/alx_travel_app_0x01.git
cd alx_travel_app_0x01

# 2. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Seed the database
python manage.py seed

# 6. (Optional) Create a superuser
python manage.py createsuperuser

# 7. Run the server
python manage.py runserver

```

## API Endpoints

- `GET /api/listings/` — List all listings  
- `POST /api/listings/` — Create a new listing  
- `GET /api/bookings/` — List all bookings  
- `POST /api/bookings/` — Create a new booking  

## Author

Project by Stevo  
GitHub: [https://github.com/Stev1000](https://github.com/Stev1000)

### 🔁 Then in terminal

```bash
git add README.md
git commit -m "Fix: clean and correct README.md for ALX checker"
git push


