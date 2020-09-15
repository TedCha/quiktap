from django.shortcuts import render
from django.views import generic

from .models import Post, Comment


class FrontPageView(generic.ListView):
    model = Post
    template_name = 'posts/front-page.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last ten posts."""
        return Post.objects.order_by('-posted_date')[:10]


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/post-detail.html'
