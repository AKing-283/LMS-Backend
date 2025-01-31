from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_lecture, name='upload_lecture'),
    path('view/', views.view_lectures, name='view_lectures'),
]