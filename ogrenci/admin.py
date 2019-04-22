from django.contrib import admin

# Register your models here.
from ogrenci.models import Ogrenci


class PostAdmin(admin.ModelAdmin):
    list_display = ['tc', 'ad_soyad', 'veli_ad', 'veli_tel']  # Listelerken Göstermek için
    list_display_links = ['tc']  # link oluşturmak için
    list_filter = ['ad_soyad', 'veli_ad']  # Filtreleme yapmak için
    list_editable = ['ad_soyad', 'veli_ad', 'veli_tel']

    class Meta:
        model = Ogrenci


admin.site.register(Ogrenci, PostAdmin)
