from django.contrib import admin

# Register your models here.
from .models import Dersler


# from .models import  DersOgrenci


class DersAdmin(admin.ModelAdmin):
    class Meta:
        model = Dersler


admin.site.register(Dersler, DersAdmin)

# class DersOgrenciAdmin(admin.ModelAdmin):
#     class Meta:
#         model = DersOgrenci
#

# admin.site.register(DersOgrenci, DersOgrenciAdmin)
