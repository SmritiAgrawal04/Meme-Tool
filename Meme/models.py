from django.db import models

# Create your models here.
class Meme(models.Model):
    userName = models.TextField()
    caption= models.TextField()
    imageURL= models.URLField()
    likes= models.BigIntegerField(default=0)