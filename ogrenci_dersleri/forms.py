from django import forms

from .models import ogrenci_dersleri


class DersOgrenciForm(forms.ModelForm):
    class Meta:
        model = ogrenci_dersleri
        fields = [
            'Id_dersogrenci',
            'ders',
            'ogrenci',

        ]



