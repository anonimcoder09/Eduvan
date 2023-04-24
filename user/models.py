from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    center_id = models.ForeignKey('center.Center', on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now=True)