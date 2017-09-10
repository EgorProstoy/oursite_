from django.db import models

# Create your models here.

class Articles(models.Model):
    id_p = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    second_name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 50)
    photo = models.ImageField(upload_to='artphoto')
    project = models.TextField()
    rent = models.IntegerField()
    def __str__(self):
        return self.second_name+' '+self.name
