from django.shortcuts import render
from .models import Recrutement, AppelsOfrres, Contrat, AMI

# Create your views here.

def recrutement(request):
    recrutements = Recrutement.objects.all()
    context = {"recrutements": recrutements}
    return render (request, 'recrutements/recrutement.html', context)

def appelsOffres(request):
    offres = AppelsOfrres.objects.all()
    context = {"offres": offres}
    return render(request, 'offres/appel-offres.html', context)

def ami(request):
    offres = AMI.objects.all()
    context = {"offres": offres}
    return render(request, 'offres/ami.html', context)