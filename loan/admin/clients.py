from django.contrib import admin
from loan.models.client import Client

class Clients(admin.ModelAdmin):
  model = Client
  
admin.site.register(Client, Clients)