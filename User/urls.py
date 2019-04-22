from django.urls import path, re_path
from .views import *

app_name = 'user'

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('ogretmenekle/', ogretmen_ekle_view, name='ogretmenEkle'),
    path('logout/', logout_view, name='logout'),

]
