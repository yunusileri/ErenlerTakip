from django.db import models
from datetime import datetime

# Create your models here.
from django.urls import reverse


def tarih_hesapla():
    tarih = str(datetime.now().astimezone())[:10]

    return tarih


def saat_hesapla():
    saat = str(datetime.now().astimezone())[11:13] + ':00'
    return saat


class Devamsizlik(models.Model):
    Id_devamsizlik = models.AutoField(primary_key=True, verbose_name='ID')
    ogrenci = models.ForeignKey('ogrenci_dersleri.ogrenci_dersleri', verbose_name='Öğrenci', on_delete=models.CASCADE,
                                related_name='Öğrenci')
    # devamsizlik_tarihi = models.CharField(max_length=10, verbose_name='Tarih', default=tarih_hesapla())
    devamsizlik_tarihi = models.DateField(default=datetime.now())
    saat = models.CharField(max_length=5, verbose_name='Saat', default=saat_hesapla())

    def __str__(self):
        return self.ogrenci.ogrenci.ad_soyad

    def devamsizlik_sil_url(self):
        return reverse('devamsizlik:sil', kwargs={'Id_devamsizlik': self.Id_devamsizlik})
