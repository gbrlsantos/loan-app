from django.db import models
from loan.models.client import Client
from loan.models.installment import Installment

class Solicitation(models.Model):
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  installment = models.ForeignKey(Installment, on_delete=models.CASCADE)
  card_number = models.IntegerField()
  desired_value = models.FloatField()
  total_loan = models.IntegerField()
