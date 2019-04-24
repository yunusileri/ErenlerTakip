from django import forms

from ogrenci.models import Ogrenci
from dersler.models import Dersler

from .models import ogrenci_dersleri


class DersOgrenciForm(forms.ModelForm):
    class Meta:
        model = ogrenci_dersleri
        fields = [
            'Id_dersogrenci',
            'ders',
            'ogrenci',
            # 'ekle'

        ]
