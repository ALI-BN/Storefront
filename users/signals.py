from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# user model will be the sender when we save


# when user is created will be recived in here
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):  # those are passed by the revicer
    if created:
        # create with the instance user we created already
        Profile.objects.create(user=instance)


# when user is created will be recived in here
@receiver(post_save, sender=User)
# kwargs accept any additional keyword argument that we are not going to use but must be passed
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  # instance is the user
