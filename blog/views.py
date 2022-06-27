from itertools import chain
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm, AddPostForm


class BlogPosts(generic.ListView):
    """
    View for displaying all the blog posts as a list
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostView(View):
    """
    View for displaying a selected post with all of its
    contents comments and likes/dislikes
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        disliked = False
        if post.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        return render(
            request,
            "post_view.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "disliked": disliked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        disliked = False
        if post.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_view.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "disliked": disliked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    """
    View for handling the likes/unlikes of a post
    making sure that the user can only like a post once
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_view', args=[slug]))


class PostDislike(View):
    """
    View for handling the dislikes/undislikes of a post
    making sure that the user can only dislike a post once
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.dislikes.filter(id=self.request.user.id).exists():
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)

        return HttpResponseRedirect(reverse('post_view', args=[slug]))


class SearchResults(generic.ListView):
    """
    View for handling the search field and its results
    """
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(court__icontains=query))
        return object_list


def add_post(request):
    """
    View for adding a new post by filling out the AddPostForm
    """
    form = AddPostForm()
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            return redirect('home')

    return render(request, 'add_post.html', context={'form': form})


class UpdatePost(UpdateView):
    """
    A view for allowing user to update a post that it is an author of
    """
    model = Post
    form_class = AddPostForm
    template_name_suffix = '_update_form'
    template_name = 'post_update_form.html'
    success_url = '/'


class DeletePost(DeleteView):
    """
    A view for allowing user to delete a post that it is an author of
    """
    model = Post
    template_name = 'confirm_delete_post.html'
    success_url = reverse_lazy('home')


class DeleteComment(DeleteView):
    """
    A view for allowing user to delete a comment that it is an author of
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('home')


class ActivityView(generic.ListView):
    """
    A view to display all posts and comments made by the user
    """
    model = Post
    model = Comment
    template_name = 'my_activity.html'

    def get_queryset(self):
        post_list = Post.objects.filter(author=self.request.user)
        comment_list = Comment.objects.filter(author=self.request.user)
        object_list = list(chain(post_list, comment_list))
        return object_list
