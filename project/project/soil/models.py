from django.db import models

class Crops(models.Model):
    Nitrogen = models.IntegerField()
    Phosphorous = models.IntegerField()
    Potassium = models.IntegerField()
    Temperature = models.IntegerField()
    Humidity = models.IntegerField()
    pH_Level = models.IntegerField()
    Rainfall = models.IntegerField()
    Crop_Name = models.CharField(max_length=50)
    class Meta:
        db_table='Crops'


class Fertilisers(models.Model):
    Nitrogen = models.IntegerField()
    Phosphorous = models.IntegerField()
    Potassium = models.IntegerField()
    pH_Level = models.IntegerField()
    Soil_Moisture = models.IntegerField()
    Crop_Name = models.CharField(max_length=50)
    class Meta:
        db_table='Fertilisers'