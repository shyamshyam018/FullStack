from django.db import models

class WorkAssignment(models.Model):
    TASK_CHOICES = (
        ('1', 'Task 1 ELECTRICAL WORK'),
        ('2', 'Task 2 PLUMBING WORK'),
        ('3', 'Task 3 EARTH WORK'),
        ('4', 'Task 4 GARDENING WORK'),
        ('5', 'Task 5 CLEANING WORK'),
        ('6', 'Task 6 OTHER MANUAL WORK'),
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

    task = models.CharField(max_length=2, choices=TASK_CHOICES)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    number_of_workers = models.IntegerField()
    duration = models.CharField(max_length=50)
    date = models.DateField()
    session = models.CharField(max_length=10)  
    work_nature = models.CharField(max_length=50) 
    staffs = models.JSONField() 
    in_time = models.TimeField()
    out_time = models.TimeField()
    status = models.CharField(max_length=20)
    remarks = models.TextField()

    def __str__(self):
        return f"Task: {self.get_task_display()}, Location: {self.get_location_display()}"
