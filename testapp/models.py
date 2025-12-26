from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    email=models.EmailField()
    location=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    