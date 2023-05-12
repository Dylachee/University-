from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import mixins, viewsets, generics, permissions
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Profile
from .permissions import IsAuthorOrReadOnly
from .serializers import ProfileSerializer
from ..partners.models import SharedFiles

User = get_user_model()


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Profile.objects.all()
    parser_classes = [MultiPartParser]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_object(self):

        if self.action == 'me':
            user = self.request.user
        else:
            user_id = self.kwargs['id']
            user = User.objects.get(pk=user_id)
        self.check_object_permissions(self.request, user)

        return user.profile

    @action(["put", "patch"], detail=False)
    def me(self, request, *args, **kwargs):
        if request.method == "PUT":
            return self.update(request, *args, **kwargs)
        elif request.method == "PATCH":
            return self.partial_update(request, *args, **kwargs)


class SharedMe(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = SharedFiles.objects.filter(user=self.request.user)
        return queryset
