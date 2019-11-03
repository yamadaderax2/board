from django.db import models

# Create your models here.
class BoardModel(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to = '')
    good = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    readtext = models.CharField(max_length=200, null=True, blank=True, default='admin')
