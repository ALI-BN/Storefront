from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# like tables in the database


class store(models.Model):
    name = models.CharField(max_length=120)
    describtion = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
