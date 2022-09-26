from django.contrib.auth import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('add_task/', AddTaskPage.as_view(), name='add_task'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('save/', save),
    path('download/', download)
]
