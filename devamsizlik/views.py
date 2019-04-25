from django.shortcuts import render, redirect
from dersler.models import Dersler
from .forms import DevamsizlikForm
from django.contrib import messages


def devamsizlik_ekle(requests):
    forms = DevamsizlikForm(requests.POST or None)
    if forms.is_valid():
        forms.save()
        messages.success(requests, 'Kayıt Başarılı')
        redirect('user:home')

    context = {'forms': forms}
    return render(requests, 'devamsizlik/Forms.html', context=context)


def devamsizlik_listele(requests):
    pass


def devamsizlik_excel(requests):
    pass


def devamsizlik_sil(requests):
    pass


def siniflari_listele(requests):
    siniflar = Dersler.objects.filter(ogretmen=requests.user)
    print(siniflar[0].ders_adi)
    return render(requests, 'home.html')
