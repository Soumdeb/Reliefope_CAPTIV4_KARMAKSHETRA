from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import DisasterReport

@csrf_exempt
def report_disaster(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        description = data.get("description")

        DisasterReport.objects.create(title=title, description=description)

        return JsonResponse({"message": "Report submitted successfully!"})
