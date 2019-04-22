from django import forms

from ogrenci.models import Ogrenci
from .models import Dersler


# from .models import DersOgrenci


class DersForm(forms.ModelForm):
    class Meta:
        model = Dersler
        fields = [
            'Id_ders',
            'ders_adi',
            'ogretmen',
        ]

# class DersOgrenciForm(forms.ModelForm):
#     class Meta:
#         model = DersOgrenci
#         fields = [
#             # 'Id_dersogrenci',
#             'ders',
#             'ogrenci',
#             # 'ekle'
#
#         ]
