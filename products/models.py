from turtle import mode
from django.db import models
from django.utils import timezone
from playground.models import store

# Create your models here.


class product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    rating = models.FloatField(default=0)
    describtion = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    sellingStore = models.ForeignKey(store, on_delete=models.CASCADE)
    image = models.ImageField(
        default='product_default.jpg', upload_to='product_pics')

    def __str__(self):
        return self.name
