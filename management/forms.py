from django import forms
from .models import WorkAssignment

class WorkAssignmentForm(forms.ModelForm):
    class Meta:
        model = WorkAssignment
        fields = [
            'task', 'location', 'number_of_workers', 'duration', 'date', 'session',
            'work_nature', 'staffs', 'in_time', 'out_time', 'status', 'remarks'
        ]
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'in_time': forms.TimeInput(attrs={'type': 'time'}),
            'out_time': forms.TimeInput(attrs={'type': 'time'}),
            'staffs': forms.Textarea(attrs={'placeholder': 'Enter staff names, separated by commas'}),
        }
