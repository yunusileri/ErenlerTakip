from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'ogretmen_mi', 'admin']  # Listelerken Göstermek için
    list_display_links = ['username']  # link oluşturmak için
    list_filter = ['username', ]  # Filtreleme yapmak için
    list_editable = ['ogretmen_mi', 'admin']

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
