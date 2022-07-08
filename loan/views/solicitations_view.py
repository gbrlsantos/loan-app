from rest_framework import viewsets
from loan.models.solicitation import Solicitation
from loan.serializers.solicitation_serializer import SolicitationSerializer

class SolicitationsViewSet(viewsets.ModelViewSet):
  queryset = Solicitation.objects.all()
  serializer_class = SolicitationSerializer