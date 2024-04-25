from django.urls import path, include   #type: ignore
from rest_framework.routers import DefaultRouter    #type: ignore
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
]
