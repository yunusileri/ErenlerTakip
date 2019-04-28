from django.shortcuts import render, redirect, get_object_or_404
from dersler.models import Dersler
from django.contrib import messages
from ogrenci_dersleri.models import ogrenci_dersleri
from .models import Devamsizlik


def devamsizlik_listele(request):
    pass


def devamsizlik_excel(request):
    pass


def devamsizlik_sil(request):
    pass


def dersi_alanlar(request, Id_ders):
    ogrenci_dersleri_obj = ogrenci_dersleri.objects.filter(ders__Id_ders=Id_ders)
    if request.POST:
        for dersogrenci in ogrenci_dersleri_obj:
            id_dersogrenci = request.POST.get(dersogrenci.ogrenci.ad_soyad)
            if id_dersogrenci is not None:
                devamsizlik = Devamsizlik()
                dersogrenci_obj = get_object_or_404(ogrenci_dersleri, Id_dersogrenci=id_dersogrenci)
                devamsizlik.ogrenci = dersogrenci_obj
                devamsizlik.save()
        messages.success(request, 'Kayıt Başarılı!')
    context = {'dersogrenci': ogrenci_dersleri_obj}
    return render(request, 'devamsizlik/dersi_alanlar.html', context=context)
