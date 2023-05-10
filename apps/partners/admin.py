from django.contrib import admin
from .models import SharedFile, Book, Project, Aim, Objective

models_to_register = [SharedFile, Book, Project, Aim, Objective]

for model in models_to_register:
    admin.site.register(model)
