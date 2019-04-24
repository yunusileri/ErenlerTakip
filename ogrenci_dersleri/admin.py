from django.contrib import admin
from .models import ogrenci_dersleri


# Register your models here.
class ogrenci_dersleri_admin(admin.ModelAdmin):
    list_display = ['ogrenci', 'ders']  # Listelerken Göstermek için
    list_display_links = ['ogrenci']  # link oluşturmak için
    list_filter = ['ders', 'ogrenci']  # Filtreleme yapmak için
    list_editable = ['ders']

    class Meta:
        model = ogrenci_dersleri


admin.site.register(ogrenci_dersleri, ogrenci_dersleri_admin)
