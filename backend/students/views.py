from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, generics
from accounts.models import Tutor
from rest_framework.response import Response
# Create your views here.
class StudentViewSet(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tutor = request.user
        print(tutor)
        students = tutor.st_tutor.all()
        print(students)
        serializer = StudentSerializer(students, many=True)
        print(serializer.data)
        return Response(serializer.data, status=200)