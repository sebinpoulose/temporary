from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def greport_login(request):
    return render(request, "greportlogin.html", {})


def login_user(request):
    logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/greports/home')
    #return render_to_response('greportlogin.html', context=RequestContext(request))
    return render(request, 'greportlogin.html', {'valid': False})


@login_required(login_url='/greports/login/')
def homepage(request):
    return render(request, "greporthome.html", {})
