from django.db import models
from loan.models.bank import Bank

class Client(models.Model):
  name = models.CharField(max_length=30)
  phone = models.IntegerField()
  cpf = models.IntegerField()
  bank = models.ForeignKey(Bank, on_delete=models.CASCADE) 