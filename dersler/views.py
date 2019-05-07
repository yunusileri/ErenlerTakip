from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DersForm
from .models import Dersler
from datetime import datetime
from User.models import User


def ders_listele(request):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')
    dersler = Dersler.objects.all()
    return render(request, 'dersler/listele.html', context={'dersler': dersler})


def ders_ekle(request):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')

    forms = DersForm(request.POST or None)
    if forms.is_valid():
        forms.save()

        messages.success(request, 'Kayıt Eklendi.')
        return redirect('dersler:listele')
    context = {'forms': forms, 'title': 'Kaydet'}
    return render(request, 'form.html', context=context)


def ders_duzenle(request, Id_ders):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')
    ders = get_object_or_404(Dersler, Id_ders=Id_ders)
    forms = DersForm(request.POST or None, instance=ders)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Başarılı Bir Şekilde Güncellediniz.')
        return redirect('dersler:listele')
    context = {'forms': forms, 'ders': ders}
    return render(request, 'dersler/GuncelleForms.html', context=context)


def ders_sil(request, Id_ders):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')
    ders = get_object_or_404(Dersler, Id_ders=Id_ders)
    ders.delete()
    messages.success(request, 'Kayıt Silindi.')
    return redirect('dersler:listele')
