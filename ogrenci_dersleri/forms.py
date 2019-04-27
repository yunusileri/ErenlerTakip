from django import forms

from .models import ogrenci_dersleri
from devamsizlik.models import Devamsizlik


class DersOgrenciForm(forms.ModelForm):
    class Meta:
        model = ogrenci_dersleri
        fields = [
            'Id_dersogrenci',
            'ders',
            'ogrenci',

        ]


class DevamsizlikForms(forms.ModelForm):
    class Meta:
        model = Devamsizlik
        fields = [

        ]
