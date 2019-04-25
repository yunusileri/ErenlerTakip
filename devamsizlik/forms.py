from django import forms
from .models import Devamsizlik


class DevamsizlikForm(forms.ModelForm):
    class Meta:
        model = Devamsizlik
        fields = [
            'ogrenci'
        ]
