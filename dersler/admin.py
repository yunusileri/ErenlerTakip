from django.contrib import admin
from .models import Dersler


class DersAdmin(admin.ModelAdmin):
    list_display = ['Id_ders', 'ders_adi', 'ogretmen']  # Listelerken Göstermek için

    class Meta:
        model = Dersler


admin.site.register(Dersler, DersAdmin)
