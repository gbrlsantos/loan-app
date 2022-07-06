from django.db import models

class Bank(models.Model):
  BANK_ACCOUNT_TYPES = [
    ('CC', 'Conta Corrente'),
    ('CP', 'Conta Poupança')
  ]
  label = models.CharField(max_length=30)
  account_type_label = models.CharField(max_length=2, choices=BANK_ACCOUNT_TYPES, default='CC')
  account_number = models.IntegerField()