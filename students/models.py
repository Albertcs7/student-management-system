from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    sname = models.CharField(max_length=15) 
    sid = models.IntegerField()
    course = models.CharField(max_length=15)
    gpa = models.FloatField()

    def __str__(self):
        return self.user.username

