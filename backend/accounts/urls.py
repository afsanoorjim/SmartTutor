from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = DefaultRouter()

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/auth/signup/', views.RegisterTutorViewSet.as_view({'post': 'create'}), name='signup'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls)),
    path("home/", views.home.as_view(), name='home')
]