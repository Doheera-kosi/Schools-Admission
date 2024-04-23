from django.urls import path, include #type: ignore
from rest_framework.routers import DefaultRouter #type: ignore
from .views import SchoolViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
]
