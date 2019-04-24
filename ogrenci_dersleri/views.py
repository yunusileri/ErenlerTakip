from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import DersOgrenciForm
from .models import ogrenci_dersleri
from dersler.models import Dersler
from ogrenci.models import Ogrenci
import pandas


def ogrenci_dersleri_ekle(request):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı goruntulemek için yetkiniz yok!')
        return redirect('user:login')

    forms = DersOgrenciForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Kayıt başarılı bir şekilde eklendi.')
        return redirect('user:home')
    context = {'forms': forms}
    return render(request, 'ogrenci_dersleri/Forms.html', context=context)


def Excel(request):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
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

    return render(request, 'ogrenci_dersleri/excelForm.html')
