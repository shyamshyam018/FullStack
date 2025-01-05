# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     ADMIN = 'admin'
#     STAFF = 'staff'
#     GUEST = 'guest'

#     ROLE_CHOICES = [
#         (ADMIN, 'Admin'),
#         (STAFF, 'Staff'),
#         (GUEST, 'Guest'),
#     ]
    
#     role = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#         return self.username
