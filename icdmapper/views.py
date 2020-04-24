import os
from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from MainProject import settings
from .forms import CutpasteForm


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


def logout_request(request):
    logout(request)
    return redirect("home")


@login_required(login_url='/icdmapper/login/')
def homepage(request):
    if request.method == 'POST':
        form = CutpasteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            field = data['diagnosis']
            answer = [('heart attack', 'I214')]
            return render(request, 'icdhome.html', {'form': form, 'answer': answer})
        else:
            print('error')
    else:
        form = CutpasteForm()
    return render(request, 'icdhome.html', {'form': form})


@login_required(login_url='/icdmapper/login/')
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = '/icdmapper'
        url = "."+fs.url(name)  # url to the file
        print(url)
        form = CutpasteForm()
        result = {'./media/37543_IurR00j.txt': [('lower respiratory tract infection', 'J22'),
                                                ('acute bronchitis', 'J209'),
                                                ('ostium secundum atrial septal defect with left to right shunt',
                                                 'Ambiguous')]}
        context = {
            'form': form,
            'url': uploaded_file.name,
            'result': result
        }
        return render(request, 'icdhome.html', context)
    form = CutpasteForm()
    return render(request, 'icdhome.html', {'form': form})


def loadstorage(request):
    if request.method == 'POST':
        filenames = request.POST.getlist('userselect')
        result = {'./media/101284.txt': [('right vocal cord polyp', 'J381')],
                  './media/109758.txt': [('metastatic adenocarcinoma prostate - post laparoscopic radical prostatectomy status', 'C61')],
                  './media/109758_rJDNRcm.txt': [('metastatic adenocarcinoma prostate - post laparoscopic radical prostatectomy status', 'C61')]}
        return render(request, 'loadstore.html',
                      {'total_files': os.listdir(settings.MEDIA_ROOT), 'path': settings.MEDIA_ROOT,
                       'result': result})
    return render(request, 'loadstore.html',
                  {'total_files': os.listdir(settings.MEDIA_ROOT), 'path': settings.MEDIA_ROOT})
