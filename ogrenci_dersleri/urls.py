from django.urls import path
from .views import *

app_name = 'dersogrenci'

urlpatterns = [
    path('ekle', ogrenci_dersleri_ekle, name='ekle'),
    path('ekle_excel', Excel, name='excel_Ekle'),
    path('siniflar', siniflari_listele, name='siniflar'),
    # path('dersialanlar/<Id_ders>', dersi_alanlar, name='dersi_alanlar')

]
