from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('delete/<str:task_name>/', views.delete_task, name='delete'),
    path('update/<str:task_name>/', views.update_task, name='update')
]