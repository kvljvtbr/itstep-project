from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.loginpage, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('delete/<str:task_name>/', views.delete_task, name='delete'),
    path('update/<str:task_name>/', views.update_task, name='update'),
    path('print-users-tasks/', views.print_users_tasks, name='print_users_tasks'),
    path('deleted-tasks/', views.deleted_tasks, name='deleted_tasks'),
    path('completed-tasks/', views.completed_tasks, name='completed_tasks'),
    path('in-progress-tasks/', views.in_progress_tasks, name='in_progress_tasks'),
]