from django.contrib.auth.models import User
from django.db import models
from djoser.serializers import UserSerializer
from rest_framework import serializers


from .models import Profile
from ..partners.serializers import SharedFilesSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user', 'organization']

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_['shared'] = SharedFilesSerializer(instance.shared_files.all(), many=True).data
        return repr_
    

class CustomUserListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        iterable = data if isinstance(data, models.Manager) else data.all()
        
        return [{
            'id': item.id,
            'username': item.username,
            'email': item.email
        } for item in iterable]


class CustomUserSerializer(UserSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('profile',)
        list_serializer_class = CustomUserListSerializer

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_['profile'] = ProfileSerializer(instance.profile).data
        return repr_