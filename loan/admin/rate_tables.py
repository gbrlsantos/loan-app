from django.contrib import admin
from loan.models.rate_table import RateTable

class RateTables(admin.ModelAdmin):
  list_diplay = ('id', 'name', 'installments')
  search_fields = ('name',)
  
admin.site.register(RateTable, RateTables)