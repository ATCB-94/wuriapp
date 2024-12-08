from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 

def contact(request):
    return render(request, 'contact.html') 

def gallerie(request):
    return render(request, 'gallerie.html') 

def atelier_regional_des_projets_WURI_6_7_et_8_mai2024(request):
    return render(request, 'atelier-regional-des-projets-WURI-6-7-et-8-mai2024.html')