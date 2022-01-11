from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(signal=post_save, sender=User)
def profile_created(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(user=user,
                                         username=user.username,
                                         email=user.email,
                                         name=user.first_name,
                                         )


@receiver(signal=post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(signal=post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

# post_save.connect(profile_created, sender=User)
# post_delete.connect(delete_user, sender=Profile)
