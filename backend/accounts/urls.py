from django.urls import include, path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tutors', views.RegisterTutorViewSet, basename='tutor')

urlpatterns = [
    path("", include(router.urls)),
    path("login/", views.RegisterTutorViewSet.as_view({'post': 'login'}), name='tutor-login')
]