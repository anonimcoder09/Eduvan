from django.db import models

class Center(models.Model):
    name = models.CharField(max_length=200, null=False)
    responsible_person = models.CharField(max_length=150, null=False)
    number = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name