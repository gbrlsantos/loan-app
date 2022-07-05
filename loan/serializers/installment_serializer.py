from rest_framework import serializers 
from loan.models.installment import Installment

class InstallmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Installment
    fields = '__all__'