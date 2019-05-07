from django import forms

from .models import Dersler


class DersForm(forms.ModelForm):
    class Meta:
        model = Dersler
        fields = [
            'ders_adi',
            'ogretmen',
        ]
