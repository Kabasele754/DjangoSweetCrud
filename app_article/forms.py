from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter title'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter description'})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
