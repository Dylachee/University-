from django.urls import path
from .views import SharedFileUploadView, SharedFileListView , BookListCreateView, BookDetailView


urlpatterns = [
    path('file.upload/', SharedFileUploadView.as_view(), name='upload'),
    path('all.file.list/', SharedFileListView.as_view(), name='list'),
    path('api/books/', BookListCreateView.as_view(), name='book_list_create'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
