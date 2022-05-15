from dataclasses import field
from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model=Postmodel
        fields=('content',)

class CommentForm(forms.ModelForm):
    commentText= forms.CharField(widget=forms.Textarea(attrs={
        'rows':'4',
    }))

    class Meta:
        model=comments
        fields= ('commentText',)