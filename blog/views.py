from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm, AddPostForm


class BlogPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostView(View):

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

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_view', args=[slug]))


class PostDislike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.dislikes.filter(id=self.request.user.id).exists():
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)

        return HttpResponseRedirect(reverse('post_view', args=[slug]))


class SearchResults(generic.ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(court__icontains=query))
        return object_list


def add_post(request):

    form = AddPostForm()
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    return render(request, 'add_post.html', context={'form': form})


class UpdatePost(UpdateView):
    model = Post
    form_class = AddPostForm
    template_name_suffix = '_update_form'
    template_name = 'post_update_form.html'
    success_url = '/'


class DeletePost(DeleteView):
    model = Post
    template_name = 'confirm_delete_post.html'
    success_url = reverse_lazy('home')
