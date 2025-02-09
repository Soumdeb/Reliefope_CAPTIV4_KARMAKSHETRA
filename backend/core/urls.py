from django.urls import path
from .views import report_disaster, create_donation, get_disaster_reports, get_donations

urlpatterns = [
    path('disasters/', get_disaster_reports, name='disaster-reports'),
    path('report/', report_disaster, name='report-disaster'),
    path('donations/', get_donations, name='donations'),
    path('donate/', create_donation, name='create-donation'),
]
