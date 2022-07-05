from django.contrib import admin
from loan.models.rate_table import Rate_Table

class Rate_Tables(admin.ModelAdmin):
  list_diplay = ('id', 'name', 'installments')
  search_fields = ('name',)
  
admin.site.register(Rate_Table, Rate_Tables)