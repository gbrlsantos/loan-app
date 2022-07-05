from rest_framework import serializers
from loan.models.rate_table import Rate_Table

class RateTableSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rate_Table
    fields = '__all__'