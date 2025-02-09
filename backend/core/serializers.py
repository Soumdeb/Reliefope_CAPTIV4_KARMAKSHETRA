#create serializers
from rest_framework import serializers
from .models import DisasterReport, Donation

class DisasterReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterReport
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
