from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Document, Image, Video, Activite, Publication_media
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'ressources/index.html') 

def document(request):
    documents = Document.objects.all()
    context = {"documents": documents}
    return render(request, 'ressources/ressources-documentaires.html', context) 

def pub_media(request):
    medias = Publication_media.objects.all()
    context = {"medias": medias}
    return render(request, 'ressources/publication-media.html', context) 

def image(request):
    images = Image.objects.all()
    context = {"images": images}
    print(context)

def activite(request):
    activites = Activite.objects.all().order_by('-id')
    context = {"activites": activites}
    return render (request, 'ressources/gallerie-activites.html', context)

def videos_activite(request):
    activites = Activite.objects.all().order_by('id')
    derniereActivites = Activite.objects.last()
    print(derniereActivites)
    context = {"activites": activites, "derniereActivite": derniereActivites}
    #return render (request, 'ressources/video-activites.html', context)
    return render (request, 'ressources/video-activites.html', context)


def gallerie(request, libele):

    
    act = Activite.objects.filter(libele=libele)
    idAct = act[0].id
    
    images = Image.objects.filter(activite=idAct)
    
    #photos = Image.objects.get(activite=libele)
    
    context = {"lib": images, "libe": libele}

    return render(request, 'ressources/libele.html', context )



def videos(request, id):

        
    videos = Video.objects.filter(activite=id)
    activites = Activite.objects.all()
    
    #photos = Image.objects.get(activite=libele)
    
    context = {"lib": videos, "activites": activites}

    return render(request, 'ressources/videos.html', context )
