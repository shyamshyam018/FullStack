from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('assign_work/', views.assign_work, name='assign_work'),
    path('generate_worksheet/', views.generate_worksheet, name='generate_worksheet'),
    path('oversee_work_status/', views.oversee_work_status, name='oversee_work_status'),
    path('manage_attendance/', views.manage_attendance, name='manage_attendance'),
    path('worker_details/', views.worker_details, name='worker_details'),
]
