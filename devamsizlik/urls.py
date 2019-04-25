from django.urls import path, re_path
from devamsizlik.views import *

app_name = 'devamsizlik'

urlpatterns = [

    path('ekle', devamsizlik_ekle, name='ekle'),
    path('siniflar', siniflari_listele, name='siniflar'),
    # path('listele', ders_listele, name='listele'),
    # path('ekle', ders_ekle, name='ekle'),
    # path('duzenle/<Id_ders>/', ders_duzenle, name='duzenle'),
    # path('sil/<Id_ders>/', ders_sil, name='sil'),
]
