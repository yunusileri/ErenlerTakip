from django.urls import path

from ogrenci_dersleri.views import ogrenci_dersleri_ekle

app_name = 'dersOgrenci'

urlpatterns = [
    path('hebele', ogrenci_dersleri_ekle, name='hebele')
]
