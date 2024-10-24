from django.contrib import admin
from .models import WorkAssignment

@admin.register(WorkAssignment)
class WorkAssignmentAdmin(admin.ModelAdmin):
    list_display = ('task', 'location', 'number_of_workers', 'duration', 'date', 'session', 'status')
