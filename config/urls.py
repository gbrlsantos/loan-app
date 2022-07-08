from django.contrib import admin
from django.urls import path, include
from loan.views.ratetables_view import RateTablesViewSet
from loan.views.solicitations_view import SolicitationsViewSet
from loan.views.clients_view import ClientViewSet
from loan.views.installments_view import InstallmentViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ratetables', RateTablesViewSet)
router.register(r'solicitations', SolicitationsViewSet)
router.register(r'clients', ClientViewSet, basename='Client')
router.register(r'installments', InstallmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
