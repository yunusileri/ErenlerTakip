from django.db import models
from django.urls import reverse


class Ogrenci(models.Model):
    tc = models.CharField(max_length=11, primary_key=True, verbose_name='Kimlik No', null=False)
    ad_soyad = models.CharField(max_length=50, verbose_name='Adı', null=False)
    dogum_tarihi = models.DateField(verbose_name='Doğum Tarihi', null=True)
    tel = models.CharField(max_length=10, verbose_name='Telefon Numarası')
    aol_no = models.CharField(max_length=10, verbose_name='AOL Num', null=True)
    veli_ad = models.CharField(max_length=50, verbose_name='Veli Adı', null=False)
    veli_tel = models.CharField(max_length=10, verbose_name='Veli Tel', null=False)
    adres = models.TextField(verbose_name='Adres', null=True)
    aktif = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.ad_soyad

    def get_update_url(self):
        return reverse('ogrenci:duzenle', kwargs={'tc': self.tc})

    @staticmethod
    def get_list_url():
        return reverse('ogrenci:listele')

    def get_delete_url(self):
        return reverse('ogrenci:sil', kwargs={'tc': self.tc})


