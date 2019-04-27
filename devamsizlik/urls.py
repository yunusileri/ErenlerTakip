from django.urls import path, re_path
from devamsizlik.views import *

app_name = 'devamsizlik'

urlpatterns = [

    path('ekle', devamsizlik_ekle, name='ekle'),
    path('listele', devamsizlik_listele, name='listele'),
    path('dersi_alanlar/<Id_ders>/', dersi_alanlar, name='dersi_alanlar'),
    path('devamsizlik_ekle_api', devamsizlik_ekle_api),

]
