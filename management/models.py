from django.db import models

# Predefined choices
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

WORK_NATURE = (
    ('manual', 'Manual'),
    ('machine', 'Machine'),
    ('other', 'Other'),
)

class Work(models.Model):
    task = models.CharField(max_length=1, choices=TASK_CHOICES)  # '1' to '6'
    work_nature = models.CharField(max_length=10, choices=WORK_NATURE)  # 'manual', 'machine', 'other'
    date = models.DateField()  # To store the date (YYYY-MM-DD format)
    session = models.CharField(max_length=10)  # Session (e.g., 'forenoon' or 'afternoon')
    in_time = models.TimeField()  # In-time (HH:MM:SS format)
    out_time = models.TimeField()  # Out-time (HH:MM:SS format)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)  # Location (from predefined choices)
    remarks = models.TextField()  # Additional remarks
    staffs = models.TextField()  # Staffs (can be a comma-separated list or JSON)
    session = models.CharField(
        max_length=10, 
        choices=SESSION_CHOICES, 
        default='forenoon'
    )

    def __str__(self):
        return f"{self.task} - {self.date} - {self.work_nature}"
