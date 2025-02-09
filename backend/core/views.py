from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import activate
from .models import DisasterReport, Donation
from .forms import DisasterReportForm
from .utils import send_sms_alert
import razorpay
import json

# Home Page
def home(request):
    return render(request, "home.html")

# Disaster Reports Page
def disaster_reports(request):
    reports = DisasterReport.objects.all()
    return render(request, "disaster_reports.html", {"reports": reports})

# Add Disaster Report (Handled via Web Extension)
@csrf_exempt
def add_disaster_report(request):
    if request.method == "POST":
        data = json.loads(request.body)
        report = DisasterReport.objects.create(
            title=data["title"],
            description=data["description"],
            location=data["location"]
        )
        # Send SMS Alert to Volunteers
        send_sms_alert("+1234567890", f"New disaster reported: {report.title}")
        return JsonResponse({"message": "Report submitted successfully"}, status=201)

    return JsonResponse({"error": "Invalid request"}, status=400)

# Donation Page
def donations(request):
    return render(request, "donations.html")

# Razorpay Donation Processing
@csrf_exempt
def process_donation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        client = razorpay.Client(auth=("YOUR_RAZORPAY_KEY", "YOUR_RAZORPAY_SECRET"))
        payment = client.order.create({
            "amount": int(data["amount"]) * 100,  # Convert to paise
            "currency": "INR",
            "payment_capture": 1
        })
        return JsonResponse({"order_id": payment["id"]})
    
    return JsonResponse({"error": "Invalid request"}, status=400)

# API for Fetching Reports (For Web Extension)
def get_disaster_reports(request):
    reports = list(DisasterReport.objects.values("title", "description", "location"))
    return JsonResponse(reports, safe=False)

def about_us(request):
    creators = [
        {"name": "Alice", "role": "Developer", "image": "creator1.jpg"},
        {"name": "Bob", "role": "Backend Engineer", "image": "creator2.jpg"},
        {"name": "Charlie", "role": "UI Designer", "image": "creator3.jpg"},
        {"name": "David", "role": "Project Manager", "image": "creator4.jpg"},
    ]
    return render(request, "about_us.html", {"creators": creators})



def choose_language(request, lang):
    activate(lang)
    return redirect("home")


def resources_awareness(request):
    resources = [
        {"title": "Emergency Preparedness Guide", "link": "https://www.ready.gov"},
        {"title": "First Aid Basics", "link": "https://www.redcross.org/firstaid"},
        {"title": "Disaster Response Plans", "link": "https://www.un.org/en/disaster-response"},
    ]
    return render(request, "resources.html", {"resources": resources})
