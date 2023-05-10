from django.contrib import admin

from .models import Aim, Book, File, Objective, Project, SharedFiles, Organization


class FileInline(admin.TabularInline):
    model = File
    extra = 3


class SharedFilesAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_by', 'upload_date']
    inlines = [FileInline]


admin.site.register(SharedFiles, SharedFilesAdmin)
admin.site.register([Book, Aim, Objective, Project, Organization])
