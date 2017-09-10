from django.db import models

# Create your models here.

class Courses(models.Model):
    logo = models.ImageField(upload_to='partphoto')
    name = models.CharField(max_length = 50)
    organization = models.CharField(max_length = 50)
    href = models.TextField()
    def __str__(self):
        return self.name
