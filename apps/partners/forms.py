from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Organization

class ArticleForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Organization
        fields = ['title', 'description']
