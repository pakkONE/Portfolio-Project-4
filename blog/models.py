from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
RATINGS = (
    (0, "0 out of 5"),
    (1, "1 out of 5"),
    (2, "2 out of 5"),
    (3, "3 out of 5"),
    (4, "4 out of 5"),
    (5, "5 out of 5")
    )


class Post(models.Model):
    """
    Post model for handling BlogPosts
    """
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    court = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=120, unique=True)
    website = models.CharField(max_length=70)
    rating = models.IntegerField(choices=RATINGS, default=5)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    court_image = CloudinaryField('image', default='placeholder')
    fragment = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='post_dislikes', blank=True)

    class Meta:
        """
        Sorts blogposts by created date,
        latest first
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        Returns the amount of likes of a post
        """
        return self.likes.count()

    def number_of_dislikes(self):
        """
        Returns the amount of dislikes of a post
        """
        return self.dislikes.count()


class Comment(models.Model):
    """
    Comments model for handling comments on posts
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_comments'
        )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Sorts comments by the order of created on
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author} on {self.created_on}"
