
from django.shortcuts import render , redirect
from .forms import WorkAssignmentForm  

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




from django.shortcuts import render, redirect
from .forms import WorkAssignmentForm
from .models import WorkAssignment 


def form_submission(request):
    if request.method == 'POST':
        form = WorkAssignmentForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('success_url')
 
    else:
        form = WorkAssignmentForm()
    return render(request, 'form_success.html', {'form': form})






def form_view(request):
    task_choices = WorkAssignment.TASK_CHOICES
    location_choices = WorkAssignment.LOCATION_CHOICES
    work_nature_choices = [('nature1', 'Nature 1'), ('nature2', 'Nature 2')]  

    if request.method == 'POST':
        form = WorkAssignment(request.POST)
        if form.is_valid():
            pass
    else:
        form = WorkAssignment()

    context = {
        'form': form,
        'task_choices': task_choices,
        'location_choices': location_choices,
        'work_nature_choices': work_nature_choices,
    }
    
    return render(request, 'form_success.html', context)
