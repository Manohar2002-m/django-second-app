from django.db import models
class Movies(models.Model):
    releasedate=models.DateField()
    moviename=models.CharField(max_length=30)
    actorname=models.CharField(max_length=30)
    actressname=models.CharField(max_length=30)
    movierating=models.FloatField()
