from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    post_id = models.CharField(max_length=10,default='')
    text = models.TextField(default='')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)