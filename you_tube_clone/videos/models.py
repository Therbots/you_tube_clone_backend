from django.db import models

# Create your models here.
class Video(models.Model):
    like = models.IntegerField()
    dislike = models.IntegerField()
    comment = models.CharField(max_length=150)