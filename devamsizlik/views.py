from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from ogrenci_dersleri.models import ogrenci_dersleri
from .models import Devamsizlik, tarih_hesapla, saat_hesapla


def devamsizlik_listele(request):
    pass


def devamsizlik_excel(request):
    pass


def devamsizlik_sil(request, Id_devamsizlik):
    # if not request.user.is_authenticated or not request.user.is_admin:
    #     messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
    #     return redirect('user:login')
    devamsizlik = get_object_or_404(Devamsizlik, Id_devamsizlik=Id_devamsizlik)
    Id_ders = str(devamsizlik.ogrenci.ders.Id_ders)
    devamsizlik.delete()
    messages.success(request, 'Kayıt Silindi.')
    return reverse('devamsizlik:duzenle', kwargs={'Id_ders': Id_ders})


def duzenle(request, Id_ders):
    devamlizliklar_obj = Devamsizlik.objects.filter(ogrenci__ders__Id_ders=Id_ders, devamsizlik_tarihi=tarih_hesapla())
    context = {'devamsizliklar': devamlizliklar_obj, 'Id_ders': Id_ders}
    return render(request, 'devamsizlik/duzenle.html', context)


def dersi_alanlar(request, Id_ders):
    ogrenci_dersleri_obj = ogrenci_dersleri.objects.filter(ders__Id_ders=Id_ders)  # Dersi alan öğrenciler bulunur.
    if request.POST:
        for ogrenci_ders_obj in ogrenci_dersleri_obj:
            id_dersogrenci = request.POST.get(
                ogrenci_ders_obj.ogrenci.ad_soyad)  # Öğrenci Adını Gönderiyor Value Değerini alıyor.

            if id_dersogrenci is not None:  # id değeri null değilse
                dersogrenci_obj = get_object_or_404(ogrenci_dersleri, Id_dersogrenci=id_dersogrenci)

                if devamsizlik_Saat_kontrol(dersogrenci_obj):
                    devamsizlik = Devamsizlik()
                    devamsizlik.ogrenci = dersogrenci_obj
                    devamsizlik.save()
                    messages.success(request, 'Kayıt Başarılı!')

    context = {'dersogrenci': ogrenci_dersleri_obj}
    return render(request, 'devamsizlik/dersi_alanlar.html', context=context)


def devamsizlik_Saat_kontrol(dersogrenci_obj):
    devamsizlik_var_mi = Devamsizlik.objects.filter(ogrenci=dersogrenci_obj,
                                                    devamsizlik_tarihi=tarih_hesapla(), saat=saat_hesapla())
    if devamsizlik_var_mi:
        return False
    else:
        return True
