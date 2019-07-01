from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import ogrenci_dersleri
from dersler.models import Dersler
from ogrenci.models import Ogrenci
import pandas


def ogrenci_ders_ekle(request):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.error(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')

    ogrenciler = Ogrenci.objects.all()
    dersler = Dersler.objects.all()
    if request.POST:
        tc = []
        dersID = []
        for ogrenci in ogrenciler:
            temp = request.POST.get(ogrenci.ad_soyad)
            if temp is not None:
                tc.append(temp)
        for ders in dersler:
            temp = request.POST.get(ders.ders_adi)
            if temp is not None:
                dersID.append(temp)
        for Id in dersID:
            ders = get_object_or_404(Dersler, Id_ders=Id)
            for temp_tc in tc:
                ogr = get_object_or_404(Ogrenci, tc=temp_tc)
                dersogr = ogrenci_dersleri(ders=ders, ogrenci=ogr)
                dersogr.save()

    context = {'ogrenciler': ogrenciler, 'dersler': dersler}

    return render(request, 'ogrenci_dersleri/ders_ekle2.html', context=context)


def Excel(request):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.error(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')

    if request.method == 'POST':
        upload_file = request.FILES['document']
        data = pandas.read_excel(io=upload_file, sheet_name=0)  # , encoding='utf-8'
        ogrenci_ders = []
        for index in range(len(data)):
            ogrenci_ders.append(ogrenci_dersleri())
            ogrenci_ders[index].ogrenci = get_object_or_404(Ogrenci, ad_soyad=data.iloc[index, 0])
            ogrenci_ders[index].ders = get_object_or_404(Dersler, ders_adi=data.iloc[index, 1])

        for i in ogrenci_ders:
            i.save()
        return redirect('user:home')

    return render(request, 'ExcelIceAktar.html')


def siniflari_listele(request):
    if not request.user.is_authenticated or not request.user.is_ogretmen_mi:
        messages.error(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')
    siniflar = Dersler.objects.filter(ogretmen=request.user)
    context = {'siniflar': siniflar}
    return render(request, 'ogrenci_dersleri/siniflarilistele.html', context=context)
