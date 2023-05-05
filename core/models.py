
from django.db import models

# Create your models here.


class Word(models.Model):
    content = models.CharField(max_length=30)
    parent_id = models.CharField(max_length=150)



class Text(models.Model):
    content = models.TextField()
    

class Analytics(models.Model):
    new_words = models.TextField()
    percentage = models.CharField(max_length=10)
