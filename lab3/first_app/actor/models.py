from re import M
from statistics import mode
from django.db import models
from django.utils.translation import gettext_lazy as _

class Actor(models.Model):
    NATIONALITIES=(
        ('ed','EGYPT'),
        ('UK','Amica'),
        ('SA','Saudi Arbia'),
    )
    GENDER=(
        ('F','female'),
        ('M','male'),
    )
    name=models.fields.CharField(verbose_name=_('Actor'),max_length=58)
    gender=models.fields.CharField(choices=GENDER,max_length=1,default='M')
    age=models.fields.PositiveIntegerField()
    nationality=models.fields.CharField(choices=NATIONALITIES,max_length=6)
    
    def __str__(self):
        return self.name
