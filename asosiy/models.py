from django.db import models

# Create your models here.
class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=30)
    tugilgan_yil = models.PositiveSmallIntegerField()
    davlat = models.CharField(max_length=30)

class Albom(models.Model):
    nom = models.CharField(max_length=30)
    sana = models.DateField()
    rasm = models.FileField(blank=True, null=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)

class Qoshiq(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=30)
    davomiylik = models.DurationField(blank=True, null=True)
    fayl = models.FileField(blank=True, null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)