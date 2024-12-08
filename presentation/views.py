from django.shortcuts import render

def index(request):
    return render(request, 'presentation/index.html') 

def composant_01(request):
    return render(request, 'presentation/composant-01.html') 

def composant_02(request):
    return render(request, 'presentation/composant-02.html') 

def composant_03(request):
    return render(request, 'presentation/composant-03.html') 


def mot_du_coordinateur(request):
    return render(request, 'presentation/mot-du-coordinateur.html') 

def mot_du_ministre(request):
    return render(request, 'presentation/mot-du-ministre.html') 