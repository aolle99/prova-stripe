from django.urls import path
from .views import procesar_pago

urlpatterns = [
    path('procesar_pago/', procesar_pago, name='procesar_pago'),
    # Otras URLs de tu proyecto
]
