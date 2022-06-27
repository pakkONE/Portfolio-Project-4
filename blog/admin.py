from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    An admin view for handling all tasks in regards to the Post model
    containing a wysiwyg editor module called Summernote
    """
    list_display = (
        'title',
        'slug',
        'status',
        'created_on',
        'updated_on',
        'court'
        )
    search_fields = ['title', 'content', 'court']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'updated_on')
    summernote_fields = ('content')
    actions = ['approve_posts']

    @admin.action(description='Mark selected stories as published')
    def approve_posts(self, request, queryset):
        queryset.update(status='1')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    An admin view for handling all tasks in regards to the Comments model
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    @admin.action(description='Approve the selected comments')
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
