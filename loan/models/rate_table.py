from django.db import models

from .installment import Installment

class Rate_Table(models.Model):
  name = models.CharField(max_length=30)
  installments = models.ManyToManyField(Installment)
  