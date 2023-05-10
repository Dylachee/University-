from rest_framework import serializers

from .models import Aim, Book, File, Objective, Project, SharedFiles , Meeting


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file']


class SharedFilesSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)

    class Meta:
        model = SharedFiles
        fields = ('id', 'title',
                  'upload_date', 'uploaded_by', 'files')
        read_only_fields = ['id', 'uploaded_by', 'profile']

    def validate(self, attrs):
        attrs['uploaded_by'] = self.context['request'].user
        return attrs

    def create(self, validated_data):
        files = validated_data.pop('files')
        shared_files = SharedFiles.objects.create(**validated_data)
        for file in files:
            File.objects.create(file=file, shared_files=shared_files)
        return shared_files

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_['files'] = FileSerializer(instance.files.all(), many=True).data
        return repr_


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description']


class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = ['id', 'description']

    def validate(self, attrs):
        attrs['aim'] = self.context['aim']
        return attrs


class AimSerializer(serializers.ModelSerializer):
    objectives = ObjectiveSerializer(many=True)

    class Meta:
        model = Aim
        fields = ['id', 'description', 'objectives']

    def validate(self, attrs):
        attrs['project'] = self.context['project']
        return attrs

    def create(self, validated_data):
        objectives = validated_data.pop('objectives')
        aim = Aim.objects.create(**validated_data)
        for objective in objectives:
            Objective.objects.create(objective=objective, aim=aim)
        return aim


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description',
                  'start_date', 'end_date', 'is_completed']
    
    def validate(self, attrs):
        user = self.context['request'].user
        if not user.profile.organization:
            raise serializers.ValidationError(
                'You must be a member of an organization to create a project')
        attrs['organization'] = user.profile.organization
        return attrs

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'