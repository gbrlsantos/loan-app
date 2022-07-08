from rest_framework import viewsets
from loan.models.installment import Installment
from loan.serializers.installment_serializer import Installment, InstallmentSerializer

class InstallmentViewSet(viewsets.ModelViewSet):
  queryset = Installment.objects.all()
  serializer_class = InstallmentSerializer