from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Profile(models.Model):
    """
    Model for User Profile. Includes User as foreign key (one to one)
    relationship alongside of a profile image and bio.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ProcessedImageField(
        upload_to='profile_images',
        default='profile_image_default.jpeg',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 60}
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
