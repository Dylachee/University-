from rest_framework import serializers
from .models import SharedFile , Book , Project, Aim, Objective

class SharedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedFile
        fields = ('id', 'title', 'description', 'upload_date', 'uploaded_by', 'file')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description']

class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = ['id', 'description']

class AimSerializer(serializers.ModelSerializer):
    objectives = ObjectiveSerializer(many=True, read_only=True)

    class Meta:
        model = Aim
        fields = ['id', 'description', 'objectives']

class ProjectSerializer(serializers.ModelSerializer):
    aims = AimSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'is_completed', 'aims']
