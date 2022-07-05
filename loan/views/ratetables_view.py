from rest_framework import viewsets
from loan.models.rate_table import RateTable
from loan.serializers.rate_table_serializer import RateTableSerializer

class RateTablesViewSet(viewsets.ModelViewSet):
  queryset = RateTable.objects.all()
  serializer_class = RateTableSerializer