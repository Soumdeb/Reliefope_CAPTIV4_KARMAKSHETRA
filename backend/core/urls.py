from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("disaster-reports/", views.disaster_reports, name="disaster_reports"),
    path("add-disaster-report/", views.add_disaster_report, name="add_disaster_report"),
    path("donations/", views.donations, name="donations"),
    path("process-donation/", views.process_donation, name="process_donation"),
    path("api/reports/", views.get_disaster_reports, name="get_disaster_reports"),
    path("about-us/", views.about_us, name="about_us"),
    path("choose-language/<str:lang>/", views.choose_language, name="choose_language"),
]
