from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import (AimListView, BookViewSet, ObjectiveCreateView,
                    SharedFileView, ProjectViewSet)

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = [
    re_path(r'projects/(?P<id>\d+)/aims/', AimListView.as_view(), name='aim_create'),
    re_path(r'aims/(?P<id>\d+)/objectives/',
         ObjectiveCreateView.as_view(), name='objective_create'),
    path('files/', SharedFileView.as_view(), name='files'),
    path('', include(router.urls), name='books'),
]
