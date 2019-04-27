from django import forms
from .models import Devamsizlik


class DevamsizlikForm(forms.Form):
    # geldi_mi = forms.BooleanField(label='Var', required=True)

    class Meta:
        model = Devamsizlik
        fields = [
            'ogrenci',
            # 'geldi_mi',
        ]
