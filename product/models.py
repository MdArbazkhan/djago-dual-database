from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30,null=True)
    weight = models.IntegerField
    price = models.IntegerField
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    class Meta:
        managed = False
        db_table = 'product'