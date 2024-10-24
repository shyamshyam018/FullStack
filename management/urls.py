from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('manage/', views.manage, name='manage'),
    path('generate_worksheet/', views.generate_worksheet, name='generate_worksheet'),
    path('oversee_work_status/', views.oversee_work_status, name='oversee_work_status'),
    path('manage_attendance/', views.manage_attendance, name='manage_attendance'),
    path('worker_details/', views.worker_details, name='worker_details'),
    path('submissionsuccess/', views.form_submission, name='submission_success'),
     path('submit/', views.form_submission, name='form_submission'),
    path('success/', TemplateView.as_view(template_name='employees/form_success.html'), name='success_url'),

]
