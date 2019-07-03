from django.contrib import admin

# Register your models here.
from .models import Devamsizlik


class DevamsizlikAdmin(admin.ModelAdmin):
    list_display = ['ogrenci', 'devamsizlik_tarihi', 'saat']  # Listelerken Göstermek için
    list_filter = ['devamsizlik_tarihi', 'ogrenci']

    class Meta:
        model = Devamsizlik


admin.site.register(Devamsizlik, DevamsizlikAdmin)
