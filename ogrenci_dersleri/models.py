from django.db import models


class ogrenci_dersleri(models.Model):
    Id_dersogrenci = models.AutoField(primary_key=True, verbose_name='Id')

    ogrenci = models.ForeignKey('ogrenci.Ogrenci', verbose_name='Öğrenci', on_delete=models.CASCADE,
                                related_name='ogrenci')
    ders = models.ForeignKey('dersler.Dersler', verbose_name='Ders', on_delete=models.CASCADE,
                             related_name='dersogrenci')

    def __str__(self):
        return self.ogrenci.ad_soyad

    # @property
    # def get_list_url(self):
    #     return reverse('dersler:dersogrencilistele')
    #
    # def get_sil_url(self):
    #     return reverse('dersler:dersogrencisil', kwargs={'Id_dersogrenci': self.Id_dersogrenci})
    #
    # def get_update_url(self):
    #     return reverse('dersler:dersogrenciduzenle', kwargs={'Id_dersogrenci': self.Id_dersogrenci})
