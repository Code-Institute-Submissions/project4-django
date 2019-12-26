from django import forms
from .models import job_database

class Newjob(forms.ModelForm):
    class Meta:
        model = job_database
        fields = (
            'company',
            'department',
            'position',
            'salary',
            'description',
        )

class Editjob(forms.ModelForm):
    class Meta:
        model = job_database
        fields = (
            'company',
            'department',
            'position',
            'salary',
            'description',
        )
        