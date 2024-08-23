
from django.shortcuts import render
from .models import Worker, WorkAssignment, Attendance

def home(request):
    return render(request, 'base.html')

def create(request):
    # Logic for assigning work
    return render(request, 'create.html')

def manage(request):
    # Logic for assigning work
    return render(request, 'manage.html')

def generate_worksheet(request):
    # Logic for generating worksheets
    return render(request, 'generate_worksheet.html')

def oversee_work_status(request):
    # Logic for overseeing work status
    return render(request, 'oversee_work_status.html')

def manage_attendance(request):
    # Logic for managing attendance
    return render(request, 'manage_attendance.html')

def worker_details(request):
    # Logic for viewing worker details
    return render(request, 'worker_details.html')

