
from django.shortcuts import render, get_object_or_404, redirect , HttpResponse
from datetime import datetime, timezone
from .forms import WorkForm
from .models import Work
from datetime import timedelta
from management.utils.dashboard_data import get_table_data , get_piechart_data , generate_dashboard_data , calculate_session_efficiency
from django.http import JsonResponse
import json

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
    task_data = get_table_data()
    filter_by = request.GET.get('filter_by', 'task')  
    chart_data = get_piechart_data(filter_by)
    graph_data = generate_dashboard_data()
    works = Work.objects.all()

  
    session_efficiency = calculate_session_efficiency(works)

    return render(request, 'base.html', {
        'tasks': task_data,
        'chart_data': json.dumps(chart_data),  
        'selected_filter': filter_by,
        'peak_time_data': json.dumps(graph_data.get('peak_time_data', {})), 
        'productivity_data': json.dumps(graph_data.get('productivity_data', {})), 
        'efficiency_data': json.dumps(list(session_efficiency.values())), 
        'location_data': json.dumps(graph_data.get('location_data', {})),  
    })





   



def manage(request):
    task_data = get_table_data() 
    return render(request, 'manage.html', {'tasks': task_data})


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


def edit_task(request, task_id):
    task = get_object_or_404(Work, id=task_id)
    
    if request.method == "POST":
        action = request.POST.get('action', '')
        
        if action == 'delete':
            # Handle the delete operation
            task.delete()
            return redirect('manage')  # Redirect to task list or some other page

        elif action == 'edit':
            
            form = WorkForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('manage', task_id=task.id)  # Redirect to task detail or some other page
    
    # Default form rendering logic
    form = WorkForm(instance=task)
    return render(request, 'edit.html', {'form': form, 'task': task})



# Delete Task View
def delete_task(request, task_id):

    task = get_object_or_404(Work, id=task_id)

    if request.method == "POST":

        task.delete()
        return redirect('manage')  


    return HttpResponse('Are you sure you want to delete this task?')


