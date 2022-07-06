from django.contrib import admin
from loan.models.rate_table import RateTable

class RateTables(admin.ModelAdmin):
  model = RateTable
  
admin.site.register(RateTable, RateTables)