from django import forms
from .models import Ogrenci


class OgrenciForm(forms.ModelForm):
    class Meta:
        model = Ogrenci
        fields = [
            'tc',
            'ad_soyad',
            'dogum_tarihi',
            'tel',
            'aol_no',
            'veli_ad',
            'veli_tel',
            'adres',
            'aktif',
        ]


class ExcelIceAktar(forms.Form):
    dosya = forms.FileField(label='Excel Dosyasını Seçiniz!')
