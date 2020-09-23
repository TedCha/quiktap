from django import forms

from .models import Post, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text_content']
        widgets = {
            'text_content': forms.Textarea(attrs={'rows': 3})
        }


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text_content']
        widgets = {
            'text_content': forms.Textarea(attrs={'rows': 3})
        }
