from __future__ import unicode_literals
from adaptor.model import CsvDbModel

from django.db import models

# Create your models here.

class Great_Britian(models.Model):
   unit_name=models.CharField(max_length=100)
   class_name=models.CharField(max_length=100)
   description=models.CharField(max_length=100000)
   men_count=models.CharField(max_length=100)
   guns=models.CharField(max_length=100)
   firepower=models.CharField(max_length=100)
   range=models.CharField(max_length=100)
   accuracy=models.CharField(max_length=100)
   reloading_skill=models.CharField(max_length=100)
   ammo=models.CharField(max_length=100)
   strength=models.CharField(max_length=100)
   speed=models.CharField(max_length=100)
   value=models.CharField(max_length=100)
   defense=models.CharField(max_length=100)


class GBcsvModel(CsvDbModel):

   class Meta:
        dbModel = Great_Britian
        delimiter=str(',')