from django.shortcuts import render
from django.views import generic

from .models import Post


class FrontPageView(generic.ListView):
    """
    Generic ListView for the front page/feed of a user.
    Displays the last 10 posts.
    """
    model = Post
    template_name = 'posts/front-page.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last ten posts."""
        return Post.objects.order_by('-posted_date')[:10]


class PostDetailView(generic.DetailView):
    """
    Generic DetailView for posts.
    """
    model = Post
    template_name = 'posts/post-detail.html'
