from django.contrib import admin
from loan.models.solicitation import Solicitation

class Solicitations(admin.ModelAdmin):
  model = Solicitation
  
admin.site.register(Solicitation, Solicitations)