from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogPosts.as_view(), name='home'),
    path('add_post/', views.add_post, name='add_post'),
    path('search/', views.SearchResults.as_view(), name='search_results'),
    path('my_activity/', views.ActivityView.as_view(), name='my_activity'),
    path('<slug:slug>/', views.PostView.as_view(), name='post_view'),
    path('edit_post/<slug:slug>', views.UpdatePost.as_view(), name='edit_post'),
    path('delete_post/<slug:slug>', views.DeletePost.as_view(), name='confirm_delete_post'),
    path('delete_comment/<int:pk>', views.DeleteComment.as_view(), name='delete_comment'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_likes'),
    path('dislike/<slug:slug>', views.PostDislike.as_view(), name='post_dislikes'),
]
