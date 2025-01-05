from django.contrib import admin
from .models import Work

@admin.register(Work)
class WorkAssignmentAdmin(admin.ModelAdmin):
    list_display = ('task','work_nature', 'location', 'in_time','out_time', 'date', 'session','remarks','staffs')
