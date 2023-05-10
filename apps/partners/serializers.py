from rest_framework import serializers
from .models import SharedFile , Book

class SharedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedFile
        fields = ('id', 'title', 'description', 'upload_date', 'uploaded_by', 'file')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description']