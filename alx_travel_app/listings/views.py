import uuid
import requests
from django.http import JsonResponse
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer


# -----------------------------
# Home Endpoint
# -----------------------------
@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome to the ALX Travel API."})


# -----------------------------
# Listings & Bookings CRUD
# -----------------------------
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# -----------------------------
# Payment Integration with Chapa
# -----------------------------
CHAPA_BASE_URL = "https://api.chapa.co/v1/transaction"
CHAPA_HEADERS = {
    "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
    "Content-Type": "application/json",
}


@api_view(["POST"])
def initiate_payment(request, booking_id):
    """
    Initiates a payment for a booking using Chapa API.
    """
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)

    # Generate unique transaction reference
    tx_ref = str(uuid.uuid4())

    # If your Booking model has total_price, use that; otherwise fallback to listing.price_per_night
    amount = getattr(booking, "total_price", booking.listing.price_per_night)

    payload = {
        "amount": str(amount),
        "currency": "ETB",
        "email": request.data.get("email", booking.user.email if hasattr(booking, "user") else "test@example.com"),
        "first_name": request.data.get("first_name", booking.user.first_name if hasattr(booking, "user") else "John"),
        "last_name": request.data.get("last_name", booking.user.last_name if hasattr(booking, "user") else "Doe"),
        "tx_ref": tx_ref,
        "callback_url": f"http://127.0.0.1:8000/payments/verify/{tx_ref}/",
        "return_url": "http://127.0.0.1:8000/payment-success/",
    }

    try:
        response = requests.post(f"{CHAPA_BASE_URL}/initialize", json=payload, headers=CHAPA_HEADERS)
        data = response.json()
    except Exception as e:
        return Response({"error": f"Failed to connect to Chapa: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if response.status_code == 200 and data.get("status") == "success":
        # Save payment record
        Payment.objects.create(
            booking=booking,
            transaction_id=tx_ref,
            amount=amount,
            status="Pending",
        )
        return Response({
            "message": "Payment initiated",
            "checkout_url": data["data"]["checkout_url"],
            "tx_ref": tx_ref
        }, status=status.HTTP_200_OK)

    return Response({"error": "Failed to initiate payment", "details": data}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def verify_payment(request, tx_ref):
    """
    Verifies payment with Chapa API using tx_ref.
    """
    try:
        payment = Payment.objects.get(transaction_id=tx_ref)
    except Payment.DoesNotExist:
        return Response({"error": "Payment record not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        response = requests.get(f"{CHAPA_BASE_URL}/verify/{tx_ref}", headers=CHAPA_HEADERS)
        data = response.json()
    except Exception as e:
        return Response({"error": f"Failed to connect to Chapa: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if response.status_code == 200 and data.get("status") == "success":
        chapa_status = data["data"]["status"]

        # Update payment record
        payment.status = "Completed" if chapa_status == "success" else "Failed"
        payment.save()

        return Response({
            "message": "Payment verified",
            "tx_ref": tx_ref,
            "status": payment.status
        }, status=status.HTTP_200_OK)

    return Response({"error": "Verification failed", "details": data}, status=status.HTTP_400_BAD_REQUEST)
