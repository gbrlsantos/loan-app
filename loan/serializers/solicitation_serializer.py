from rest_framework import serializers
from loan.models.solicitation import Solicitation
from loan.models.installment import Installment
from loan.serializers.client_serializer import ClientSerializer
from loan.serializers.installment_serializer import InstallmentSerializer

class SolicitationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Solicitation
    fields = ('client', 'installment', 'card_number', 'desired_value', 'total_loan')
    
  def to_representation(self, instance):
    response = super().to_representation(instance)
    response['installment'] = InstallmentSerializer(instance.installment).data
    return response
      