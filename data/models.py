from __future__ import unicode_literals
from adaptor.model import CsvDbModel
from django.db import models




# Create your models here.
class Adult(models.Model):





    name = models.CharField(max_length=20)


    hpG = models.CharField(max_length=10)
    strG = models.CharField(max_length=10)
    magG = models.CharField(max_length=10)
    skillG = models.CharField(max_length=10)
    spdG = models.CharField(max_length=10)
    lckG = models.CharField(max_length=10)
    defG = models.CharField(max_length=10)
    resG = models.CharField(max_length=10)

    strB = models.CharField(max_length=10)
    magB = models.CharField(max_length=10)
    skillB = models.CharField(max_length=10)
    spdB = models.CharField(max_length=10)
    lckB = models.CharField(max_length=10)
    defB = models.CharField(max_length=10)
    resB = models.CharField(max_length=10)

    sex = models.CharField(max_length=10)
    classP = models.CharField(max_length=30)
    class2 = models.CharField(max_length=30)

class AdultcsvModel(CsvDbModel):

   class Meta:
        dbModel = Adult
        delimiter=str(',')