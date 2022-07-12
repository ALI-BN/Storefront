from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from playground.models import store
# Create your models here.


class Profile(models.Model):
    # if the user is deleted  profile will as will but not the way around
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_pics the directory of the images files
    image = models.ImageField(
        default='picture_default.jpg', upload_to='profile_pics')
    # stores = models.ForeignKey(store.name, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
