from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model for User Profile. Includes User as foreign key (one to one)
    relationship alongside of a profile image and bio.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile_image_default.jpeg',
        upload_to='profile_images'
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
