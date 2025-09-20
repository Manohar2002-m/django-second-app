from django.db import models

# Create your models here.
class student(models.Model):
    sname=models.CharField(max_length=30)
    srollno=models.IntegerField()
    smarks=models.IntegerField()
    semial=models.EmailField()
    

