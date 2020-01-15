from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CutpasteForm
# Create your views here.


def icdmapper_login(request):
    return render(request, "icdmapperlogin.html", {})


def login_user(request):
    logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/icdmapper/home')
    return render(request, 'icdmapperlogin.html', {'valid': False})


#@login_required(login_url='/icdmapper/login/')
#def homepage(request):
#    return render(request, "icdhome.html", {})


@login_required(login_url='/icdmapper/login/')
def logout_request(request):
    logout(request)
    # return render(request, "Home_page.html", {})
    return redirect("home")


@login_required(login_url='/icdmapper/login/')
def homepage(request):
    if request.method == 'POST':
        form = CutpasteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            feild=data['diagnosis']
            answer = feild
            print(feild)
            return render(request, 'icdhome.html', {'form': form, 'answer': answer})
        else:
            print('error')
    else:
        form = CutpasteForm()
    return render(request, 'icdhome.html', {'form': form})


