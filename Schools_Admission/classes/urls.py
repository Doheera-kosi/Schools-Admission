from django.urls import path, include #type: ignore
from rest_framework.routers import DefaultRouter  #type: ignore
from .views import ClassViewSet, SchoolClassesViewSet

router = DefaultRouter()
router.register(r'classes', ClassViewSet, basename='classes')

urlpatterns = [
    path('', include(router.urls)),
    path('schools/<int:pk>/classes/', SchoolClassesViewSet.as_view({'get': 'list'}), name='school-classes-list'),
    
    path('classes/<int:pk>/enroll/', ClassViewSet.as_view({'post': 'enroll_student'}), name='class-enroll'),


]
