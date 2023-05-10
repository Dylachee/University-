from django.db import models
from django.contrib.auth.models import User

class SharedFile(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='shared_files/')

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Aim(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='aims')
    description = models.TextField()

    def __str__(self):
        return self.description

class Objective(models.Model):
    aim = models.ForeignKey(Aim, on_delete=models.CASCADE, related_name='objectives')
    description = models.TextField()

    def __str__(self):
        return self.description
