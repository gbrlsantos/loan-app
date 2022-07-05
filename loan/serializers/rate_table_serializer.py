from rest_framework import serializers
from loan.models.rate_table import RateTable
from loan.serializers.installment_serializer import InstallmentSerializer

class RateTableSerializer(serializers.ModelSerializer):
  installments = InstallmentSerializer(read_only=True, many=True)
  class Meta:
    model = RateTable
    fields = ('name', 'installments')