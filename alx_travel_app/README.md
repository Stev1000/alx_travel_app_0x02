# alx_travel_app_0x02

This is a Django RESTful application for managing travel listings, bookings, and payments with **Chapa API**.

## Milestone 4: Payment Integration with Chapa API

This project integrates Chapa Payment Gateway for secure payment processing in a travel booking application.

## Features Implemented

- Payment Model: Created Payment model in listings/models.py to track transactions
- Payment Initiation: API endpoint to initiate payments via Chapa API  
- Payment Verification: API endpoint to verify payment status
- Secure Credentials: API keys stored in environment variables
- Payment Workflow: Complete booking and payment flow integration
- Error Handling: Graceful handling of payment failures
- Email Notifications: Confirmation emails sent on successful payments

## Project Structure

- listings/models.py — Contains Payment model and booking models
- listings/views.py — Payment initiation and verification endpoints
- alx_travel_app/ — Main project settings and URL configuration
- requirements.txt — Python dependencies including Chapa integration

## Technologies Used

- Python 3
- Django 3.2
- Django REST Framework
- Chapa API for payments
- PostgreSQL
- Celery for background tasks
- Requests library for API calls

## Payment Integration

This application successfully integrates with Chapa API to:

1. Initiate secure payments for travel bookings
2. Verify payment statuses  
3. Update booking records based on payment results
4. Send confirmation emails on successful transactions

The payment integration is fully tested using Chapa's sandbox environment.
