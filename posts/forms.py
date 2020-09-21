from django import forms

from .models import Post


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text_content', 'image_content']
        widgets = {
            'text_content': forms.Textarea(attrs={'rows': 3})
        }
