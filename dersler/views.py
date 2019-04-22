from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Dersler
from .forms import DersForm
from ogrenci.models import Ogrenci


# from .forms import  DersOgrenciForm

# from .models import  DersOgrenci

def ders_Listele(request):
    dersler = Dersler.objects.all()
    return render(request, 'dersler/listele.html', context={'dersler': dersler})


def ders_Ekle(request):
    forms = DersForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Kayıt Eklendi.')
        return redirect('dersler:listele')
    context = {'forms': forms}
    return render(request, 'dersler/Forms.html', context=context)


def ders_Duzenle(request, Id_ders):
    ders = get_object_or_404(Dersler, Id_ders=Id_ders)
    forms = DersForm(request.POST or None, instance=ders)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Başarılı Bir Şekilde Güncellediniz.')
        return redirect('dersler:listele')
    context = {'forms': forms, 'ders': ders}
    return render(request, 'dersler/GuncelleForms.html', context=context)


def ders_Sil(request, Id_ders):
    ders = get_object_or_404(Dersler, Id_ders=Id_ders)
    ders.delete()
    messages.success(request, 'Kayıt Silindi.')
    return redirect('dersler:listele')

#
# def dersogrenci_Listele(request):
#     dersogrenciler = DersOgrenci.objects.all()
#     return render(request, 'dersler/dersogrenciListele.html', context={'dersogrenciler': dersogrenciler})
#
#
# def dersogrenci_Ekle(request):
#     forms = DersOgrenciForm(request.POST or None)
#     ogrenci = Ogrenci.objects.all()
#     dersler = Dersler.objects.all()
#     if forms.is_valid():
#         forms.save(commit=False)
#         # id_ders = forms.cleaned_data.get('ders').Id_ders
#
#         c = forms.cleaned_data.get('name')
#         print(c)
#         # print(b.Id_ders)
#         # print(forms.eklensin_mi)
#         # print(forms)
#         print('Eklendi')
#         messages.success(request, 'Kayıt Eklendi.')
#         return redirect('dersler:dersogrencilistele')
#     context = {'forms': forms, 'ogrenciler': ogrenci, 'dersler': dersler}
#     return render(request, 'dersler/dersogrenciForm.html', context=context)
#
#
# def dersogrenci_Duzenle(request, Id_dersogrenci):
#     dersogrenci = get_object_or_404(Dersler, Id_dersogrenci=Id_dersogrenci)
#     forms = DersOgrenciForm(request.POST or None, instance=dersogrenci)
#     if forms.is_valid():
#         forms.save()
#         messages.success(request, 'Başarılı Bir Şekilde Güncellediniz.')
#         return redirect('dersler:dersogrenciekle')
#     context = {'forms': forms, 'dersogrenci': dersogrenci}
#     return render(request, 'dersler/GuncelleForms.html', context=context)
#
#
# def dersogrenci_Sil(request, Id_dersogrenci):
#     dersogrenci = get_object_or_404(DersOgrenci, Id_dersogrenci=Id_dersogrenci)
#     dersogrenci.delete()
#     messages.success(request, 'Kayıt Silindi.')
#     return redirect('dersler:dersogrencilistele')
