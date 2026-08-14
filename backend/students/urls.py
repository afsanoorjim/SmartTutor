from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views



urlpatterns = [
    path('students/', views.StudentViewSet.as_view(), name='student_list')
]