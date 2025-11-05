from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name