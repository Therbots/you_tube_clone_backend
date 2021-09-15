from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Video(models.Model):
    video_id = models.CharField(max_length=50)
    like = models.IntegerField()
    dislike = models.IntegerField()
    comment = models.CharField(max_length=150)
    reply = models.CharField(max_length=150)