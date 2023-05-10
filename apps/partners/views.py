from typing import Any
from django import http
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Aim, Book, Objective, Project, SharedFiles
from .serializers import (AimSerializer, BookSerializer, ObjectiveSerializer,
                          ProjectSerializer, SharedFilesSerializer)


class SharedFileView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SharedFilesSerializer
    queryset = SharedFiles.objects.filter(user=None)


class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class AimListView(generics.ListCreateAPIView):
    serializer_class = AimSerializer

    def setup(self, request, *args: Any, **kwargs: Any) -> None:
        super().setup(request, *args, **kwargs)
        self.project = get_object_or_404(
            Project.objects, id=self.kwargs.get('id'))

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Aim.objects.none()
        return Aim.objects.filter(project=self.project)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if not getattr(self, 'swagger_fake_view', False):
            context['project'] = self.project
        return context


class ObjectiveCreateView(generics.CreateAPIView):
    serializer_class = ObjectiveSerializer

    def setup(self, request, *args: Any, **kwargs: Any) -> None:
        super().setup(request, *args, **kwargs)
        self.aim = get_object_or_404(Aim.objects, id=self.kwargs.get('id'))

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Objective.objects.none()
        return Objective.objects.filter(aim=self.aim)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if not getattr(self, 'swagger_fake_view', False):
            context['aim'] = self.aim
        return context
