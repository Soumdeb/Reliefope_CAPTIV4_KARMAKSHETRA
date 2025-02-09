from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import VolunteerForm

def register_volunteer(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = VolunteerForm()
    return render(request, "volunteers/register.html", {"form": form})
