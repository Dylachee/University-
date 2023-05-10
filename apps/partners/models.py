from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Organization(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.title


class SharedFiles(models.Model):
    user = models.ForeignKey(
        'auth.User', related_name='shared_files', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class File(models.Model):
    shared = models.ForeignKey(
        SharedFiles, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='shared_files/')


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name='projects', default=None)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Aim(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='aims')
    description = models.TextField()

    def __str__(self):
        return self.description


class Objective(models.Model):
    aim = models.ForeignKey(Aim, on_delete=models.CASCADE,
                            related_name='objectives')
    description = models.TextField()

    def __str__(self):
        return self.description

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='meeting_photos/', blank=True, null=True)
    video = models.FileField(upload_to='meeting_videos/', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.title
# TODO
# class Meeting(models.Model):
# class Report(models.Model):
