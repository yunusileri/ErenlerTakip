from django.urls import path

from ogrenci.views import *

app_name = 'ogrenci'
urlpatterns = [

    path('listele', ogrenci_listele, name='ogrencilistele'),
    path('ekle', ogrenci_ekle, name='ogrenciekle'),
    path('ekle_excel', excel_ice_aktar_ogrenci, name='excel_Ekle'),
    path('excel_disa_aktar', ogrencileri_excele_aktar, name='excel_disa_aktar'),
    path('duzenle/<tc>/', ogrenci_duzenle, name='ogrenciduzenle'),
    path('sil/<tc>/', ogrenci_sil, name='ogrencisil'),

]
