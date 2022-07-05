from django.contrib import admin
from django.urls import path, include
from loan.views.ratetables_view import RateTablesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ratetables', RateTablesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
