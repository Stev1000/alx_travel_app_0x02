from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ListingViewSet, BookingViewSet
from .views import initiate_payment, verify_payment


router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls)),
    
]
