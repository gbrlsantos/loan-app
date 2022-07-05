from rest_framework import serializers
from loan.models.rate_table import RateTable

class RateTableSerializer(serializers.ModelSerializer):
  class Meta:
    model = RateTable
    fields = '__all__'