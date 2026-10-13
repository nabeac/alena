from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models.warehouse import Warehouse
# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField

class User(AbstractUser):
    STATUS_USER = (
        ('a',"active"),
        ('d',"deactive")
    )
    
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField()
    status = models.CharField(max_length=1, choices=STATUS_USER, default='a')
    is_manager = models.BooleanField(default=False)
    last_visited = models.DateTimeField(auto_now=True)

    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.username