from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoSensorViewSet, LeituraSensorViewSet, receber_dados

router = DefaultRouter()
router.register(r'tipos', TipoSensorViewSet)
router.register(r'leituras', LeituraSensorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('receber-dados/', receber_dados, name='receber_dados'),
]
