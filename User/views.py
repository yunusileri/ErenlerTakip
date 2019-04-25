from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


#
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        # username = request.POST['user_name']
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('user:home')
    return render(request, 'accounts/form.html', {'forms': form, 'title': 'Giriş Yap'})


def ogretmen_ekle_view(request):
    if not request.user.is_authenticated or not request.user.is_admin:
        messages.success(request, 'Bu sayfayı görüntülemek için izniniz yok!')
        return redirect('user:login')
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.ogretmen_mi = True


        user.save()
        new_user = authenticate(request, username=user.username, password=password)
        login(request, new_user)
        return redirect('user:home')

    return render(request, 'accounts/form.html', {'forms': form, 'title': 'Kaydet'})


def logout_view(request):
    logout(request)
    return redirect('user:home')


def home_view(request):
    return render(request, 'home.html', {'title': 'Anasayfa'})
