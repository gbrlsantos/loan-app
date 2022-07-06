from django.contrib import admin
from loan.models.installment import Installment

class Installments(admin.ModelAdmin):
  model = Installment
  
admin.site.register(Installment, Installments)