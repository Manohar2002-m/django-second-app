from django.db import models
class Movies(models.Model):
    release_date=models.DateField()
    moivename=models.CharField(max_length=50)
    actorname=models.CharField(max_length=50)
    actressname=models.CharField(max_length=50)
    rating=models.FloatField()
# Create your models here.
