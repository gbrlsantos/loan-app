from rest_framework import serializers
from loan.models.solicitation import Solicitation
from loan.serializers.client_serializer import ClientSerializer
from loan.serializers.installment_serializer import InstallmentSerializer

class SolicitationSerializer(serializers.ModelSerializer):
  client = ClientSerializer(read_only=True, many=False)
  installment = InstallmentSerializer(read_only=True, many=False)
  
  class Meta:
    model = Solicitation
    fields = '__all__'