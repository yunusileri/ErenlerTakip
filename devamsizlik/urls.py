from django.urls import path, re_path
from devamsizlik.views import *

app_name = 'devamsizlik'

urlpatterns = [
    path('listele', devamsizlik_listele, name='listele'),
    path('listele/<tarih>/', devamsizlik_listele),
    path('listele/<tarih>/<ders>/', devamsizlik_listele),
    path('listele/<tarih>/<ders>/<TC>/', devamsizlik_listele),

    path('duzenle/<Id_ders>/', duzenle, name='duzenle'),
    path('dersi_alanlar/<Id_ders>/', dersi_alanlar, name='dersi_alanlar'),
    path('devamsizlik_sil/<Id_devamsizlik>/', devamsizlik_sil, name='sil'),

]
