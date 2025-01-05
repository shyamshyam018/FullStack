from django import forms
from .models import Work

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['date', 'session', 'task', 'work_nature', 'in_time', 'out_time', 'location', 'remarks', 'staffs']
        widgets = {
            'session': forms.Select(attrs={'class': 'form-control'}),  # Render session as a dropdown
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'in_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'out_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }