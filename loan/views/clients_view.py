from rest_framework import viewsets
from loan.models.client import Client
from loan.serializers.client_serializer import Client, ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
  serializer_class = ClientSerializer
  
  def get_queryset(self):
    queryset = Client.objects.all()
    cpf = self.request.query_params.get('cpf')
    if cpf is not None:
      queryset = queryset.filter(cpf=cpf)
    return queryset