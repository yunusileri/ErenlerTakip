from django.shortcuts import render
from .forms import DersOgrenciForm
from django.contrib import messages
from django.shortcuts import redirect


def ogrenci_dersleri_ekle(request):
    if not request.user.is_authenticated or request.user.is_admin:
        messages.success(request, 'Bu sayfayı goruntulemek için yetkiniz yok!')
        return redirect('user:login')
    forms = DersOgrenciForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Kayıt başarılı bir şekilde eklendi.')
        return redirect('user:home')
    context = {'forms': forms}
    return render(request, 'ogrenci_dersleri/Forms.html', context=context)
