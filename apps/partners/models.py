from django.db import models
from django.contrib.auth.models import User
from ..user.models import Profile


class SharedFile(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='shared_files/')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='shared_files')

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
