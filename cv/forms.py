from django import forms
from .models import CVrecord

class PostCVrecord(forms.ModelForm):

    class Meta:
        model = CVrecord
        fields = ("name", "record_type", "details", "start_date", "end_date")

