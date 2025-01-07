from management.models import Work
from datetime import datetime
from collections import Counter
from django.db.models import Count
import matplotlib.pyplot as plt
import matplotlib
from datetime import timedelta
matplotlib.use('Agg')

LOCATION_CHOICES = (

    ('Location 1', 'BOYS HOSTEL'),
    ('Location 2', 'GIRLS HOSTEL'),
    ('Location 3', 'STAFF QUARTERS'),
    ('Location 4', 'AS BLOCK'),
    ('Location 5', 'IB BLOCK'),
    ('Location 6', 'SF BLOCK'),
    ('Location 7', 'MECH BLOCK'),
    ('Location 8', 'AERO/RESEARCH BLOCK'),
    ('Location 9', 'MEDICAL CENTER'),
)

TASK_CHOICES = (
    ('1', 'Task 1 ELECTRICAL WORK'),
    ('2', 'Task 2 PLUMBING WORK'),
    ('3', 'Task 3 EARTH WORK'),
    ('4', 'Task 4 GARDENING WORK'),
    ('5', 'Task 5 CLEANING WORK'),
    ('6', 'Task 6 OTHER MANUAL WORK'),
)

SESSION_CHOICES = (
    ('forenoon', 'Forenoon'),
    ('afternoon', 'Afternoon'),
)


WORK_NATURE = (
    ('manual', 'Manual'),
    ('machine', 'Machine'),
    ('other', 'Other'),
)



def get_table_data():
    tasks = Work.objects.all()  
    task_data = []
    for task in tasks:
        location_name = task.get_location_display()

        # Calculate total hours
        if task.in_time and task.out_time:  
            today = datetime.today().date() 
            start_time = datetime.combine(today, task.in_time)
            end_time = datetime.combine(today, task.out_time)

            time_difference = end_time - start_time
            total_hours = time_difference.seconds // 3600  
        else:
            total_hours = 0

        # Count workers
        staff_names = task.staffs  
        worker_count = len([name.strip() for name in staff_names.split(",") if name.strip()])

        # Append processed data
        task_data.append({
            'id': task.id,
            'work_nature':task.work_nature,
            'location': location_name,
            'total_hours': total_hours,
            'worker_count': worker_count,
            'session': task.session
            
        })

    return task_data






TASK_MAP = dict(TASK_CHOICES)
SESSION_MAP = dict(SESSION_CHOICES)
LOCATION_MAP = dict(LOCATION_CHOICES)
WORK_NATURE_MAP = dict(WORK_NATURE)

def get_piechart_data(filter_by):
    tasks = Work.objects.all()

    if filter_by == "location":     
        data = Work.objects.values('location').annotate(task_count=Count('id'))
        labels = [LOCATION_MAP[task['location']] for task in data] 
        values = [task['task_count'] for task in data]
        return {"labels": labels, "values": values}

    elif filter_by == "task":
        data = Work.objects.values('task').annotate(task_count=Count('id'))
        labels = [TASK_MAP[task['task']] for task in data] 
        values = [task['task_count'] for task in data]

        return {"labels": labels, "values": values}

    elif filter_by == "session":
        data = Work.objects.values('session').annotate(task_count=Count('id'))
        labels = [SESSION_MAP[task['session']] for task in data] 
        values = [task['task_count'] for task in data]

        return {"labels": labels, "values": values}

    elif filter_by == "work_nature":
        data = Work.objects.values('work_nature').annotate(task_count=Count('id'))
        labels = [WORK_NATURE_MAP[task['work_nature']] for task in data] 
        values = [task['task_count'] for task in data]
        return {"labels": labels, "values": values}

    else:
        labels = []
        values = []

    return {"labels": labels, "values": values}




def generate_dashboard_data():
    # Query all the tasks (works)
    works = Work.objects.all()

    # Peak Time Graph - Number of tasks per hour
    hour_labels = list(range(8, 20))  # Labels for hours 8AM to 7PM
    hour_data = [0] * len(hour_labels)  # Initialize count array

    for work in works:
        hour = work.in_time.hour  # Extract hour from the in_time field
        if hour in hour_labels:
            index = hour_labels.index(hour)
            hour_data[index] += 1

    # Productivity Graph - Hours worked per day
    daily_productivity = {}
    for work in works:
        date = work.date
        duration = (
            timedelta(hours=work.out_time.hour, minutes=work.out_time.minute)
            - timedelta(hours=work.in_time.hour, minutes=work.in_time.minute)
        )
        duration_in_hours = duration.total_seconds() / 3600  # Convert seconds to hours
        daily_productivity[date.strftime('%Y-%m-%d')] = daily_productivity.get(date.strftime('%Y-%m-%d'), 0) + duration_in_hours
        
    # Efficiency and Other Stats Graph
    session_efficiency = {'forenoon': 0, 'afternoon': 0}
    for work in works:
        session_efficiency[work.session] += 1

    # Location-wise task distribution
    location_data = {}
    for work in works:
        location_data[work.location] = location_data.get(work.location, 0) + 1

    return {
        'peak_time_data': hour_data,
        'productivity_data': daily_productivity,
        'efficiency_data': session_efficiency,
        'location_data': location_data,
    }
