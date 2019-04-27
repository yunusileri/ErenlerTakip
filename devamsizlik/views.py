from django.shortcuts import render, redirect, get_object_or_404
from dersler.models import Dersler
from .forms import DevamsizlikForm
from django.contrib import messages
from ogrenci_dersleri.models import ogrenci_dersleri
from .models import Devamsizlik


def devamsizlik_ekle(request):
    forms = DevamsizlikForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Kayıt Başarılı')
        # redirect('user:home')

    context = {'forms': forms}
    return render(request, 'devamsizlik/Forms.html', context=context)


def devamsizlik_listele(request):
    pass


def devamsizlik_excel(request):
    pass


def devamsizlik_sil(request):
    pass


def dersi_alanlar(request, Id_ders):
    dersogrencis = ogrenci_dersleri.objects.filter(ders__Id_ders=Id_ders)
    if request.POST:
        for dersogrenci in dersogrencis:
            c = request.POST.get(dersogrenci.ogrenci.ad_soyad)
            if c is not None:
                devamsizlik = Devamsizlik()
                dersogrenci_obj = get_object_or_404(ogrenci_dersleri, Id_dersogrenci=c)
                devamsizlik.ogrenci = dersogrenci_obj
                devamsizlik.save()

    context = {'dersogrenci': dersogrencis}
    return render(request, 'devamsizlik/dersi_alanlar.html', context=context)


def devamsizlik_ekle_api(request):
    devamsizlik = Devamsizlik()
    devamsizlik.ogrenci = request.GET.get('ogrenci')
    devamsizlik.save()
