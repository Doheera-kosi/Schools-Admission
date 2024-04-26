from django.urls import path, include #type: ignore
from rest_framework.routers import DefaultRouter #type: ignore
from .views import SchoolViewSet
from .views import SchoolStudentsDetailView


router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='schools')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('schools/<int:pk>/students/', SchoolStudentsDetailView.as_view(), name='school-students-detail'),
    
    path('schools/<int:pk>/full/', SchoolViewSet.as_view({'get': 'school_full_status'}), name='school-full-status'),

]
