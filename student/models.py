from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150 ,null=False)
    number = models.CharField(max_length=20, null=False)
    paid = models.BooleanField()
    group_id = models.ForeignKey('group.Group', null=False, on_delete=models.CASCADE)
    center_id = models.ForeignKey('center.Center', null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.first_name, self.last_name