from django.db import models

# Create your models here.

class Alternatif(models.Model):
    kri=models.TextField(null=True,blank=True)
    umur=models.TextField(null=True,blank=True)
    gaji=models.TextField(null=True,blank=True)
    luas=models.TextField(null=True,blank=True)