import pandas
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from ogrenci.forms import OgrenciForm
from ogrenci.models import Ogrenci
from ogrenci.excel_aktarim import *


def ogrencileri_excele_aktar(request):
    ogrenciler = Ogrenci.objects.all()
    ogrencileri_al(ogrenciler)
    response = HttpResponse(open(f'{BASE_DIR}/static/öğrenciler.xls', 'rb').read())
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Content-Disposition'] = f'attachment; filename=ogrenciler.xls'
    return response


def home_view(request):
    return render(request, 'home.html', {'title': 'Anasayfa'})


def ogrenci_listele(request):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')
    ogrenciler = Ogrenci.objects.all()

    return render(request, 'ogrenci/listele.html', {'ogrenciler': ogrenciler})


def ogrenci_ekle(request):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')
    forms = OgrenciForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Kayıt Eklendi', extra_tags='Mesaj Başarılı')
        return redirect('ogrenci:ogrencilistele')
    context = {'forms': forms}
    return render(request, 'ogrenci/ogrenci_ekle_form.html', context)


def excel_ice_aktar_ogrenci(request):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')

    if request.method == 'POST':
        upload_file = request.FILES['document']
        data = pandas.read_excel(io=upload_file, sheet_name=0)
        for index in range(len(data)):
            ogrenci = Ogrenci()
            ogrenci.tc = data.iloc[index, 0]
            ogrenci.ad_soyad = data.iloc[index, 1]
            ogrenci.dogum_tarihi = data.iloc[index, 2]
            ogrenci.tel = data.iloc[index, 3]
            ogrenci.aol_no = data.iloc[index, 4]
            ogrenci.veli_ad = data.iloc[index, 5]
            ogrenci.veli_tel = data.iloc[index, 6]
            ogrenci.adres = data.iloc[index, 7]
            ogrenci.aktif = data.iloc[index, 8]
            ogrenci.save()

        return redirect('ogrenci:ogrencilistele')

    return render(request, 'ExcelIceAktar.html')


def ogrenci_duzenle(request, tc):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')

    ogrenci = get_object_or_404(Ogrenci, tc=tc)
    forms = OgrenciForm(request.POST or None, instance=ogrenci)

    if forms.is_valid():
        forms.save()
        messages.success(request, 'Başarılı Bir Şekilde Güncellediniz.')
        return HttpResponseRedirect(ogrenci.get_list_url())
    context = {'forms': forms, 'ogrenci': ogrenci}
    return render(request, 'ogrenci/updateForm.html', context)


def ogrenci_sil(request, tc):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')
    ogrenci = get_object_or_404(Ogrenci, tc=tc)
    ogrenci.delete()
    messages.success(request, 'Kayıt Silindi.')
    return redirect('ogrenci:ogrencilistele')
