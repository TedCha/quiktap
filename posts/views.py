from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic

from .models import Post
from .forms import PostModelForm


class PostListView(generic.ListView):
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


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Generic CreateView for users to create posts.
    """
    model = Post
    template_name = 'posts/post-form.html'
    form_class = PostModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    Generic CreateView for users to create posts.
    """
    model = Post
    template_name = 'posts/post-form.html'
    form_class = PostModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    Generic DeleteView for posts.
    """
    model = Post
    template_name = 'posts/post-delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
