__author__ = 'lorgio'
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

class Post(models.Model):
    author = models.ForeignKey(User, related_name='post')
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

class Photo(models.Model):
    post = models.ForeignKey(Post, related_name='photos')
    image = models.ImageField(upload_to="%Y%m%d")