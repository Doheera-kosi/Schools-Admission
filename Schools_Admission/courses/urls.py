from django.urls import path, include #type: ignore
from rest_framework.routers import DefaultRouter #type: ignore
from .views import CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
]
