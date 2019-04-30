import pandas
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import OgrenciForm
from .models import Ogrenci
from django.contrib.auth.decorators import login_required


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
    return render(request, 'ogrenci/form.html', context)


def Excel(request):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')

    if request.method == 'POST':
        upload_file = request.FILES['document']
        data = pandas.read_excel(io=upload_file, sheet_name=0)  # , encoding='utf-8'
        ogrenciler = []
        for index in range(len(data)):
            ogrenciler.append(Ogrenci())
            ogrenciler[index].tc = data.iloc[index, 0]
            ogrenciler[index].ad_soyad = data.iloc[index, 1]
            ogrenciler[index].dogum_tarihi = data.iloc[index, 2]
            ogrenciler[index].tel = data.iloc[index, 3]
            ogrenciler[index].aol_no = data.iloc[index, 4]
            ogrenciler[index].veli_ad = data.iloc[index, 5]
            ogrenciler[index].veli_tel = data.iloc[index, 6]
            ogrenciler[index].adres = data.iloc[index, 7]
        for ogrenci in ogrenciler:
            ogrenci.save()
        return redirect('ogrenci:ogrencilistele')

    return render(request, 'ogrenci/excelForm.html')


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
