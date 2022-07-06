from rest_framework import serializers
from loan.models.client import Client
from loan.serializers.bank_serializer import BankSerializer

class ClientSerializer(serializers.ModelSerializer):
  bank = BankSerializer(read_only=True, many=False)
  class Meta:
    model = Client
    fields = ('name', 'phone', 'cpf', 'bank')