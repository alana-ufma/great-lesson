from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import EditAccountForm, ChangePasswordForm, RegisterForm, PasswordResetForm, PasswordResetFormConfirm
from .models import PasswordReset
from aula.models import *

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'Usuário autenticado!')
      return redirect('accounts:dashboard')
    else:
      messages.error(request, 'Credenciais Inválidas. Tente Novamente')
      return redirect('accounts:login')
  else:
    return render(request, 'accounts/login.html')


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Usuário desconectado!')
    return redirect('accounts:login')


def register(request):
    pass

@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = ChangePasswordForm(data= request.POST, user=request.user)
        if form.is_valid():
            form.save()
            #form = PasswordChangeForm(instance=request.user)
            context['success'] = True
    else:
        form = ChangePasswordForm(user=request.user)

    context['form'] = form

    return render(request, template_name, context)


def password_reset(request):
    pass
def password_reset_confirm(request):
    pass




def dashboard(request):
    context = {'aulas': Aula.objects.all().filter(criador=request.user)}
    template_name ='accounts/dashboard.html'
    return render(request, template_name, context)


@login_required
def profile(request):
    context = {}
    template_name ='accounts/profile.html'
    return render(request, template_name, context)


@login_required
def edit_profile(request):
    template_name = 'accounts/edit_profile.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)

    context['form'] = form

    return render(request, template_name, context)
