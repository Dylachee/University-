from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import SharedFile , Book , Project, Aim, Objective
from .serializers import SharedFileSerializer , BookSerializer , ProjectSerializer, AimSerializer, ObjectiveSerializer


class SharedFileUploadView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = SharedFileSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

class SharedFileListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SharedFileSerializer
    queryset = SharedFile.objects.all()

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class AimCreateView(generics.CreateAPIView):
    serializer_class = AimSerializer

class ObjectiveCreateView(generics.CreateAPIView):
    serializer_class = ObjectiveSerializer