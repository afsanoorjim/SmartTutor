from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Tutor
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterTutorSerializer
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView




class home(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.headers)
        return HttpResponse('logged in successfully', request.user.name)


class RegisterTutorViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Tutor.objects.all()
    serializer_class = RegisterTutorSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

