from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DisasterReport, Donation
from .serializers import DisasterReportSerializer, DonationSerializer
import razorpay
from django.conf import settings
from twilio.rest import Client


@api_view(['POST'])
def report_disaster(request):
    serializer = DisasterReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        send_sms_alert(serializer.data['location'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def send_sms_alert(location):
    account_sid = 'your_twilio_sid'
    auth_token = 'your_twilio_auth_token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Urgent! Disaster reported at {location}. Immediate help needed!",
        from_='+your_twilio_number',
        to='+recipient_number'
    )
    return message.sid

@api_view(['POST'])
def create_donation(request):
    serializer = DonationSerializer(data=request.data)
    if serializer.is_valid():
        client = razorpay.Client(auth=('your_razorpay_key', 'your_razorpay_secret'))
        payment = client.order.create({"amount": int(request.data['amount']) * 100, "currency": "INR", "payment_capture": '1'})
        serializer.save(status='Processing')
        return Response({'order_id': payment['id']}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_disaster_reports(request):
    reports = DisasterReport.objects.all()
    serializer = DisasterReportSerializer(reports, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_donations(request):
    donations = Donation.objects.all()
    serializer = DonationSerializer(donations, many=True)
    return Response(serializer.data)
