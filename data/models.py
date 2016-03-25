from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Adult(models.Model):
    #classFE =
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    #classChar = models.CharField(choices=classFE)
    hpG = models.IntegerField()
    strG = models.IntegerField()
    magS = models.IntegerField()
    skillG = models.IntegerField()
    spdG = models.IntegerField()
    lckG = models.IntegerField()
    defG = models.IntegerField()
    resG = models.IntegerField()
    hpB = models.IntegerField()
    strB = models.IntegerField()
    magB = models.IntegerField()
    skillB = models.IntegerField()
    spdB = models.IntegerField()
    lckB = models.IntegerField()
    defB = models.IntegerField()
    resB = models.IntegerField()