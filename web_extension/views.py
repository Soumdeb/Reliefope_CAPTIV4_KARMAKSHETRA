from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def report_disaster(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        description = data.get("description")


        return JsonResponse({"message": "Report submitted successfully!"})
