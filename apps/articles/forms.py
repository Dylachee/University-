from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Article

class ArticleForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ['title', 'description', 'image']
