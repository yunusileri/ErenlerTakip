from django.contrib import admin

# Register your models here.

from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']  # Listelerken Göstermek için

    list_display_links = ['username']  # link oluşturmak için

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
