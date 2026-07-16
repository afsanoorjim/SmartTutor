from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Tutor
from .serializers import RegisterTutorSerializer
from django.contrib.auth import authenticate, login

class RegisterTutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = RegisterTutorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def login(self, request, *args, **kwargs):
        # Implement your login logic here
        email = request.data.get('email')
        password = request.data.get('password')
        tutor = get_object_or_404(Tutor, email=email)
        if tutor.check_password(password):
            # Return a success response or token
            login(request, tutor)
            return Response({'message': 'Login successful'})
        else:
            return Response({'message': 'Invalid credentials'}, status=401)

