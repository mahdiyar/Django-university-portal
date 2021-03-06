from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

"""
class users(models.Model):
 #   Id = models.IntegerField
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=150)
    accessLevel=models.IntegerField()
    email = models.EmailField()
"""

class course(models.Model):
 #   courseID = models.IntegerField
    name= models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    teacher = models.ForeignKey(User)
    status = models.BooleanField()
    Date = models.DateField()

class studentList(models.Model):
 #   Id = models.IntegerField
    course = models.ForeignKey(course)
    student = models.ForeignKey(User)
    point = models.FloatField()


