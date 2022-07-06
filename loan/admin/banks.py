from django.contrib import admin
from loan.models.bank import Bank

class Banks(admin.ModelAdmin):
  model = Bank

admin.site.register(Bank, Banks)