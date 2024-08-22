
from django.shortcuts import render
from .models import Worker, WorkAssignment, Attendance

def home(request):
    return render(request, 'home.html')

def assign_work(request):
    # Logic for assigning work
    return render(request, 'assign_work.html')

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

