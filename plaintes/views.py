from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Faq, plainte, glossaire
from .forms import plainteForm

# Create your views here.

def faq(request):
    faqs = Faq.objects.all()
    context = {"faqs": faqs}
    return render(request, 'faqs/index.html', context)


#GESTION DES PLAINTES

#Formulaire pour enregister la plainte
def soumettre_une_requette(request):
    return render(request, 'requetes/soumettre-une-requette.html')

#Fonction pour enregistrer la plainte dans la base de donnees non utilisé
def add_plainte(request):

    nom = request.POST.get('nom')
    email = request.POST.get('email')
    telephone = request.POST.get('telephone')
    objet = request.POST.get('objet')
    message = request.POST.get('message')
    traitement = 1 
    plainte = plainte(nom=nom, email=email, telephone=telephone, objet=objet, message=message, traitement=traitement)
    plainte.save()
    #plainte = plainte(nom=nom, email=email, telephone=telephone, objet=objet, message=message, traitement=traitement)
    # plainte.save()
    #return render(request, 'plaintes/soumettre-une-requette.html')
    context = {"nom": nom, "email": email, "telephone": telephone, "objet": objet, "message": message, "traitement": traitement}
    return redirect('faq.html')
    #return render(request, 'soumettre-une-requette.html')

#Fonction pour enregistrer la plainte dans la base de donnée utilisée
def plainte_create_view(request):
    if request.method == 'POST':
        form = plainteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq')
    else:
        form = plainteForm()
    return render(request, 'requetes/create.html', {'form': form})

#Formulaire pour rechercher une plainte enregistré
def suivi_plainte(request):
    return render(request, 'requetes/suivre-le-traitement-requette.html')

#Recherche de la plainte
def recherche(request):
    if request.method == 'POST':
        plaint = plainte.objects.filter(nom=request.POST.get('nom'))
        context = {'plaintes': plaint}
        return render(request, 'requetes/suivre-le-traitement-requette.html', context)
    return HttpResponse(plaint)

#GESTION DU GLOSSAIRE

#Formulaire de recherche du glossaire
def glassaire(request):
    glossaires = glossaire.objects.all()
    context = {"glossaires": glossaires}
    return render(request, 'glossaire/home.html', context)

def rech_glossaire(request):
    glossaires = glossaire.objects.filter(mot__contains=request.POST.get('terme'))
    context = {"termes": glossaires}
    return render(request, 'glossaire/rech_terme.html', context)

