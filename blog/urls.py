from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogPosts.as_view(), name='home'),
    path('<slug:slug>/', views.PostView.as_view(), name='post_view'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_likes'),
    path('dislike/<slug:slug>', views.PostDislike.as_view(), name='post_dislikes'),
]