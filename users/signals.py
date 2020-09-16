from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal for post saving of a instance in the User Model. If the
    User instance was created rather than edited, we create a profile
    for the User instance.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Signal for post saving of an instance in the User Model. If the
    User Model is edited, save the profile too.
    """
    instance.profile.save()
