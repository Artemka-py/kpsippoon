from django.core.checks import messages
from django.http.response import Http404
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from .models import Changes, Product
from django.contrib.auth import login, authenticate, logout

def index(req):
    changes = Changes.objects.order_by('-id')
    last = Product.objects.order_by('-id').first()
    return render(req, 'project/index.html', context={'changes': changes, 'last': last})

def change_detail(req, change_id):
    try:
        change = Changes.objects.get(pk=change_id)
        product = Product.objects.get(pk=change.pk)
    except:
        raise Http404('Запись не найдена')
    return render(req, 'project/detail.html', context={'change': change, 'product': product})
        

def logout_view(request):
    logout(request)
    return redirect('home')

def auth(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Логин или пароль не верны!')
    context= {}
    return render(request, 'registration/login.html', context=context)

def registretion_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registration/registr.html', context)