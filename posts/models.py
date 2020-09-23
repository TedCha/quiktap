from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """
    Model for Posts.
    """
    text_content = models.CharField(max_length=160)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text_content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    """
    Model for Comments on Posts.
    """
    text_content = models.CharField(max_length=160)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text_content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})
