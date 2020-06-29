from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import NewsletterForm
from .models import NewsletterSubscription


def index(request):
    context = {}
    form = NewsletterForm(request.POST or None)
    print('aqui 1')
    if form.is_valid():
        print('aqui 2')
        name = request.POST['name']
        email = request.POST['email']

        if NewsletterSubscription.objects.filter(email=email):
            messages.error(request,'Este email já foi cadastrado anteriormente!')
        else:
            subscription = NewsletterSubscription(name=name, email=email)

            subscription.save()
            form = NewsletterForm()
            messages.success(request,'Sua inscrição foi realizada!')

    context['form'] = form
    template_name = 'index.html'
    return render(request, template_name, context)

    # template_name = 'index.html'
    # context = {}
    # return render(request,template_name, context)


def home(request):
    context = {}
    form = NewsletterForm(request.POST or None)
    print('aqui 1')
    if form.is_valid():
        print('aqui 2')
        name = request.POST['name']
        email = request.POST['email']

        if NewsletterSubscription.objects.filter(email=email):
            messages.error(request,'Este email já foi cadastrado anteriormente!')
        else:
            subscription = NewsletterSubscription(name=name, email=email)

            subscription.save()
            form = NewsletterForm()
            messages.success(request,'Sua inscrição foi realizada!')

    context['form'] = form
    template_name = 'home.html'
    return render(request, template_name, context)


def catalogo(request):
    template_name = 'catalogo.html'
    context = {'aulas': get_aulas()}
    return render(request,template_name, context)
