from django.db import models

# Create your models here.
from django.db import models
#Create your models here.
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=64)
    ssub=models.CharField(max_length=64)
    scollege=models.CharField(max_length=256)
def __str__(self):
        return str(self.sno)+"\t"+self.sname+"\t"+str(self.ssub)+"\t"+self.scollege;



