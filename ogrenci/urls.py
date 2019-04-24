from django.urls import path

from ogrenci.views import *

app_name = 'ogrenci'
urlpatterns = [


    path('listele', ogrenci_listele, name='ogrencilistele'),
    path('ekle', ogrenci_ekle, name='ogrenciekle'),
    path('ekle_excel', Excel, name='excel_Ekle'),
    path('duzenle/<tc>/', ogrenci_duzenle, name='ogrenciduzenle'),
    path('sil/<tc>/', ogrenci_sil, name='ogrencisil'),

]
