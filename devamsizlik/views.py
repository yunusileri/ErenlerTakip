from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from ogrenci_dersleri.models import ogrenci_dersleri
from .models import Devamsizlik, tarih_hesapla, saat_hesapla
from datetime import datetime, timedelta
from dersler.models import Dersler
from ogrenci.models import Ogrenci


def devamsizlik_listele(request, tarih="Bugün", ders='', TC=''):
    devamsizliklar = devamsizlik_Tarih_Filtrele(tarih, ders, TC)
    dersler = Dersler.objects.all()
    ogrenciler = Ogrenci.objects.all()
    context = {'devamsizliklar': devamsizliklar, 'dersler': dersler, 'ogrenciler': ogrenciler}
    return render(request, "devamsizlik/listele.html", context=context)


def devamsizlik_Tarih_Filtrele(tarih, ders, TC):
    tarihler = {'Bugün': 0, 'Haftalık': 7, 'Aylık': 30, 'Yıllık': 365}
    days = tarihler[tarih]
    aralik = datetime.today() - timedelta(days=days)
    if ders == '':
        if TC == '':
            devamsizliklar = Devamsizlik.objects.filter(devamsizlik_tarihi__gte=aralik,
                                                        devamsizlik_tarihi__lte=datetime.now())
        else:
            devamsizliklar = Devamsizlik.objects.filter(devamsizlik_tarihi__gte=aralik,
                                                        devamsizlik_tarihi__lte=datetime.now(),
                                                        ogrenci__ogrenci__tc=TC)
    else:
        if TC == '':
            devamsizliklar = Devamsizlik.objects.filter(devamsizlik_tarihi__gte=aralik,
                                                        devamsizlik_tarihi__lte=datetime.now(),
                                                        ogrenci__ders__ders_adi=ders)
        else:
            devamsizliklar = Devamsizlik.objects.filter(devamsizlik_tarihi__gte=aralik,
                                                        devamsizlik_tarihi__lte=datetime.now(),
                                                        ogrenci__ders__ders_adi=ders,
                                                        ogrenci__ogrenci__tc=TC)
    return devamsizliklar


def devamsizlik_excel(request):
    pass


def devamsizlik_sil(request, Id_devamsizlik):
    if not request.user.is_authenticated or not request.user.is_ogretmen_mi:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')

    devamsizlik = get_object_or_404(Devamsizlik, Id_devamsizlik=Id_devamsizlik)
    devamsizlik.delete()
    messages.success(request, 'Kayıt Silindi.')
    return redirect('dersogrenci:siniflar')


def duzenle(request, Id_ders):
    devamlizliklar_obj = Devamsizlik.objects.filter(ogrenci__ders__Id_ders=Id_ders,
                                                    devamsizlik_tarihi=tarih_hesapla())
    context = {'devamsizliklar': devamlizliklar_obj, 'Id_ders': Id_ders}
    return render(request, 'devamsizlik/duzenle.html', context)


def dersi_alanlar(request, Id_ders):
    Dersi_alan_ogrenciler = ogrenci_dersleri.objects.filter(ders__Id_ders=Id_ders)  # Dersi alan öğrenciler bulunur.
    if request.POST:
        for ogr_obj in Dersi_alan_ogrenciler:
            id_dersogrenci = request.POST.get(ogr_obj.ogrenci.tc)  # Öğrenci tc Gönderiyor Value Değerini alıyor.
            print(id_dersogrenci)
            if id_dersogrenci is not None:

                dersogrenci_obj = get_object_or_404(ogrenci_dersleri, Id_dersogrenci=id_dersogrenci)

                if devamsizlik_Saat_kontrol(dersogrenci_obj):
                    devamsizlik = Devamsizlik()
                    devamsizlik.ogrenci = dersogrenci_obj
                    devamsizlik.save()
                    messages.success(request, 'Kayıt Başarılı!')

    context = {'dersogrenci': Dersi_alan_ogrenciler}
    return render(request, 'devamsizlik/dersi_alanlar.html', context=context)


def devamsizlik_Saat_kontrol(dersogrenci_obj):
    devamsizlik_var_mi = Devamsizlik.objects.filter(ogrenci=dersogrenci_obj,
                                                    devamsizlik_tarihi=tarih_hesapla(), saat=saat_hesapla())
    if devamsizlik_var_mi:
        return False
    else:
        return True
