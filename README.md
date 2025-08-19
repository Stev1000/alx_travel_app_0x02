# alx_travel_app_0x02

This is a Django RESTful application for managing travel listings, bookings, and payments with **Chapa API**.

## Project Overview
This project is part of the ALX Software Engineering program.

## Project Structure
- `listings/` — Django app containing models, serializers, and seed logic  
- `alx_travel_app/` — Main project settings and URL configuration  
- `requirements.txt` — Python dependencies  
- `README.md` — Project setup and documentation  

## Features
- Create and view travel listings  
- Book available listings by date  
- Make secure payments via **Chapa API**  

## Technologies Used
- Python 3  
- Django 3.2  
- Django REST Framework  
- Chapa API  

## Setup Instructions
```bash
# 1. Clone the repository
git clone https://github.com/Stev1000/alx_travel_app_0x02.git
cd alx_travel_app_0x02

# 2. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. (Optional) Create a superuser
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
