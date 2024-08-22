from django import forms
from .models import Task

class TaskAssignmentForm(forms.ModelForm):
    class Meta:
        model =  Task
        fields = ['task_id', 'nature_of_work', 'location', 'number_of_workers', 'duration', 'feedback']

    def clean(self):
        cleaned_data = super().clean()
        number_of_workers = cleaned_data.get('number_of_workers')
        staff_names = []

        for i in range(number_of_workers):
            staff_name = cleaned_data.get(f'staff_name_{i + 1}')
            if staff_name:
                staff_names.append(staff_name)

        cleaned_data['staff_names'] = staff_names

        return cleaned_data
