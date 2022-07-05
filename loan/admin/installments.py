from django.contrib import admin
from loan.models.installment import Installment

class Installments(admin.ModelAdmin):
  list_diplay = ('__all__')
  
admin.site.register(Installment, Installments)