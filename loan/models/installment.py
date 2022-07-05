from django.db import models

class Installment(models.Model):
  number = models.IntegerField()
  interest = models.FloatField()
  value = models.FloatField()
  full_value = models.FloatField()
  comission = models.FloatField()
  