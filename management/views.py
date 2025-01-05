
from django.shortcuts import render , redirect
from datetime import datetime, timezone
from django.shortcuts import render, redirect
from .forms import WorkForm

def create(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form = WorkForm()

    return render(request, 'create.html', {'form': form})



def profile_view(request):
    user = request.user
    if user.last_login:
        now = datetime.now(timezone.utc)
        time_diff = now - user.last_login
        hours = time_diff.total_seconds() // 3600
        minutes = (time_diff.total_seconds() % 3600) // 60
        last_login_display = f"{int(hours)} hours and {int(minutes)} minutes ago"
    else:
        last_login_display = "Never logged in"

    context = {
        'user': user,
        'last_login_display': last_login_display,
    }
    return render(request, 'profile.html', context)

def home(request):
    return render(request, 'base.html')


    if request.method == 'POST':
        form = WorkAssignmentForm(request.POST)
        
        # Manually checking if the form has errors
        if form.is_bound and not form.errors:
            # If no errors, save the form data
            form.save()
            return redirect('success')  # Redirect to success page
        else:
            # If there are errors, return to the form with error messages
            return render(request, 'create.html', {'form': form})
    else:
        form = WorkAssignmentForm()

    task_choices = WorkAssignment.TASK_CHOICES
    location_choices = [
        ('1', 'Electrical Work'),
        ('2', 'Plumbing Work'),
        ('3', 'Earth Work'),
        ('4', 'Gardening Work'),
        ('5', 'Cleaning Work'),
        ('6', 'Other Manual Work'),
    ]
    work_nature_choices = [
        ('manual', 'Manual'),
        ('machine', 'Machine'),
        ('other', 'Other'),
    ]
    
    context = {
        'form': form,
        'task_choices': task_choices,
        'location_choices': location_choices,
        'work_nature_choices': work_nature_choices
    }
    
    return render(request, 'create.html', context)

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

def success(request):
    return render(request, 'form_success.html')


# from django.shortcuts import render, redirect
# from .forms import WorkAssignmentForm
# from .models import WorkAssignment 


# def form_submission(request):
#     if request.method == 'POST':
#         form = WorkAssignmentForm(request.POST)
#         if form.is_valid():
#             form.save() 
#             return redirect('success_url')
 
#     else:
#         form = WorkAssignmentForm()
#     return render(request, 'form_success.html', {'form': form})






# def form_view(request):
#     task_choices = WorkAssignment.TASK_CHOICES
#     location_choices = WorkAssignment.LOCATION_CHOICES
#     work_nature_choices = [('nature1', 'Nature 1'), ('nature2', 'Nature 2')]  

#     if request.method == 'POST':
#         form = WorkAssignment(request.POST)
#         if form.is_valid():
#             pass
#     else:
#         form = WorkAssignment()

#     context = {
#         'form': form,
#         'task_choices': task_choices,
#         'location_choices': location_choices,
#         'work_nature_choices': work_nature_choices,
#     }
    
#     return render(request, 'form_success.html', context)
