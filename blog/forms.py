from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'court',
            'location',
            'website',
            'rating',
            'content',
            'court_image',
            'fragment'
            ]
        
