from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
    Form to submit a comment on a post
    """
    class Meta:
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    """
    Form to submit a new post as registered user
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'court',
            'location',
            'website',
            'rating',
            'content',
            'court_image',
            'fragment'
            ]
