from django.db import models


# Create your models here.


class Devamsizlik(models.Model):
    Id_devamsizlik = models.AutoField(primary_key=True, verbose_name='ID')
    ogrenci = models.ForeignKey('ogrenci_dersleri.ogrenci_dersleri', verbose_name='Öğrenci', on_delete=models.CASCADE,
                                related_name='Öğrenci')
    devamsizlik_tarihi = models.DateTimeField(verbose_name='Tarih', auto_now_add=True)

    def __str__(self):
        return self.ogrenci.ogrenci.ad_soyad
