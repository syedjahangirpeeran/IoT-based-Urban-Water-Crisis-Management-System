from __future__ import unicode_literals
from django.db import models
class Sensors(models.Model):
    serialId=models.CharField(default="Not Received",max_length=100)
    sensor1=models.FloatField(default=0)
    sensor2=models.FloatField(default=0)
    sensor3=models.FloatField(default=0)
    sensor4=models.FloatField(default=0)
    sensor5=models.FloatField(default=0)
    sensor6=models.FloatField(default=0)
    time=models.CharField(default="Not Received",max_length=100)
    def __str__(self):
        return str(self.serialId)+' '+str(self.sensor1)+' '+str(self.sensor2)+' '+str(self.sensor3)+' '+str(self.sensor4)+' '+str(self.sensor5)+' '+str(self.sensor6)+' '+str(self.time)