from django.db import models
from requests import delete
from experiments.models import Experiment
from django.utils.html import format_html

class Device(models.Model):
    #id
    company         = models.CharField(max_length=127)
    model           = models.CharField(max_length=127)

    def __str__(self):
        return f"{self.company}: {self.model}"

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

class Measurement(models.Model):
    #id
    experiment      = models.ForeignKey(Experiment, on_delete=models.PROTECT, related_name="getMeasurement")
    device          = models.ForeignKey(Device, on_delete=models.PROTECT)
    file            = models.FileField(upload_to='measurements/')
    is_approved     = models.BooleanField(default=True)                             #set to False in production
    #type (NMR, Mn, ...) -> is this a Device or Measurement attribute?

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Measurement'
        verbose_name_plural = 'Measurements'

class Data(models.Model):
    #id
    measurement     = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name="getData")       #if a measurement gets deleted, delete the data as well.
    res_time        = models.FloatField()
    result          = models.FloatField()
    #is_outlier     a function can identify outliers and set this flag so this data can be hidden if needed