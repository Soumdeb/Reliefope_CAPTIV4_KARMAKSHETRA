from django.urls import path
from .views import register_volunteer

urlpatterns = [
    path("register/", register_volunteer, name="volunteer_register"),
]
