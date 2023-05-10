from django.urls import path
from .views import (
    SharedFileUploadView, 
    SharedFileListView , 
    BookListCreateView, 
    BookDetailView , 
    ProjectListCreateView,
    ProjectDetailView,
    AimCreateView,
    ObjectiveCreateView,)


urlpatterns = [
    path('file.upload/', SharedFileUploadView.as_view(), name='upload'),
    path('all.file.list/', SharedFileListView.as_view(), name='list'),
    path('api/books/', BookListCreateView.as_view(), name='book_list_create'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('api/projects/', ProjectListCreateView.as_view(), name='project_list_create'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('api/aims/', AimCreateView.as_view(), name='aim_create'),
    path('api/objectives/', ObjectiveCreateView.as_view(), name='objective_create'),
]
