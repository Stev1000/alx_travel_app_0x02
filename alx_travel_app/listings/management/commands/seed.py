from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from alx_travel_app.listings.models import Listing, Booking, Review
from django.utils import timezone
import random
from datetime import timedelta, date

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **kwargs):
        # Create Users
        for i in range(5):
            username = f'user{i}'
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    email=f'{username}@example.com',
                    password='password123'
                )
        self.stdout.write(self.style.SUCCESS('✅ Created sample users'))

        users = list(User.objects.all())

        # Create Listings
        for i in range(5):
            Listing.objects.create(
                title=f'Cozy Room {i}',
                description='A beautiful room in the city center.',
                price_per_night=random.uniform(40, 120),
                location=f'Location {i}'
            )
        self.stdout.write(self.style.SUCCESS('✅ Created sample listings'))

        listings = list(Listing.objects.all())

        # Create Bookings
        for _ in range(5):
            check_in = date.today() + timedelta(days=random.randint(1, 10))
            check_out = check_in + timedelta(days=random.randint(1, 5))
            Booking.objects.create(
                listing=random.choice(listings),
                user=random.choice(users),
                check_in=check_in,
                check_out=check_out
            )
        self.stdout.write(self.style.SUCCESS('✅ Created sample bookings'))

        # Create Reviews
        for _ in range(5):
            Review.objects.create(
                listing=random.choice(listings),
                user=random.choice(users),
                rating=random.randint(1, 5),
                comment="Very nice place, would stay again!"
            )
        self.stdout.write(self.style.SUCCESS('✅ Created sample reviews'))
