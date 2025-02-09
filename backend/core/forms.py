from django import forms
from .models import DisasterReport

class DisasterReportForm(forms.ModelForm):
    class Meta:
        model = DisasterReport
        fields = ['title', 'description', 'location']
