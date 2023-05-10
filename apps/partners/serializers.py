from rest_framework import serializers
from .models import SharedFile , Book

class SharedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedFile
        fields = ('id', 'title', 'description', 'upload_date', 'uploaded_by', 'file')
        read_only_fields = ['id', 'uploaded_by', 'profile']

    def create(self, validated_data):
        validated_data['uploaded_by'] = self.context['request'].user
        validated_data['profile'] = self.context['request'].user.profile
        return super().create(validated_data)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description']