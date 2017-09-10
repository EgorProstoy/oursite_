from django.db import models

# Create your models here.

class Party_policy(models.Model):
    idea = models.TextField()
    text = models.TextField()    
    def __str__(self):
        return self.idea[:300]

class Person(models.Model):
    person_name = models.CharField(max_length = 50)
    person_family = models.CharField(max_length = 50, primary_key = True)
    person_info = models.CharField(max_length = 50)
    def __str__(self):
        return person_name+' '+person_family+'\n'+person_info[:100]
