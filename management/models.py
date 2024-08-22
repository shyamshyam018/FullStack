
from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    # Add other fields as needed

class WorkAssignment(models.Model):
        TASK_CHOICES = (
            ('1', 'Task 1 ELETRICAL WORK'),
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

        task_id = models.CharField(max_length=50, choices=TASK_CHOICES)
        nature_of_work = models.CharField(max_length=100)
        location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
        number_of_workers = models.IntegerField()
        staff_names = models.JSONField(default=list)  # Storing as JSON array
        duration = models.CharField(max_length=50)
        feedback = models.TextField(blank=True)
        worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
        description = models.TextField()
        assigned_date = models.DateField()
        due_date = models.DateField()

        def __str__(self):
            return f"Task ID: {self.task_id}, Location: {self.location}"
    # Add other fields as needed

class Attendance(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # e.g., 'Present', 'Absent'
    # Add other fields as needed
