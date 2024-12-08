from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Post
from django.core.paginator import Paginator


def index(request):

    actualites = [
        {
            'titre_court': 'Atelier regional du WURI',
            'titre_long': "Identification biométrique dans l’espace CEDEAO : plus de 100 millions de personnes visées par le projet WURI",
            'image': "img/melsa/020.JPG",
            'auteur': "Wuri",
            'date': "21-04-2024",
            'ville': "Abidjan",
            'contenu': "<p>Abidjan, le 07 mai 2024 – A l’occasion d’un atelier sur la revue du Projet d’identification unique pour l’intégration régionale de l’inclusion en Afrique de l’Ouest (WURI), le 06 mai 2024 à Abidjan, la directrice pays de la Banque mondiale pour la Côte d’Ivoire, le Bénin, la Guinée et le Togo, Marie Chantal Uwanyiligira, a indiqué que le projet WURI ambitionne de donner un identifiant à plus de 100 millions de personnes dans l’espace CEDEAO.</p> <p>« La CEDEAO compte à peu près 330 millions de personnes et parmi eux, 196 millions n’ont pas d’identifiant, ce qui veut dire qu’ils ne sont pas connus de leur gouvernement. Le projet WURI a pour ambition de donner un identifiant à plus de 100 millions de personnes », a déclaré Marie Chantal Uwanyiligira.</p> <p>Selon elle, le projet WURI vise à transformer positivement la vie des populations et permettre aux gouvernements de planifier le développement des pays. Et d’assurer que la Banque mondiale ne lésinera pas sur ses moyens pour permettre à ces personnes d’obtenir des documents d’identité.</p> <p>Pour le ministre de l’Emploi et de la Protection sociale, Adama Kamara, le projet WURI est en cohérence avec la vision du Président Alassane Ouattara qui a décidé de faire de la protection sociale un levier important de son développement économique.</p> <p>L’identifiant unique, de l’avis du ministre, permettra aux populations d’avoir accès, outre à la nationalité, aux services sociaux de base, notamment, les services de développement du capital humain, l’inclusion financière et économique.</p> <p>Il a rappelé que la Côte d’Ivoire a réussi, à fin 2023, à enrôler biométriquement plus de 10 millions des résidents grâce au programme WURI et vise l’identification de 20 millions de résidents fin 2024. </p> <p>Notons que cet atelier régional devrait permettre aux participants d’être situés sur l’état de mise en œuvre du projet WURI et de partager les expériences pour renforcer la coordination, nécessaire à l’interopérabilité régionale.</p>",
        },
        {
            'titre_court': 'Atelier regional du WURI',
            'titre_long': "Identification biométrique dans l’espace CEDEAO : plus de 100 millions de personnes visées par le projet WURI",
            'image': "img/melsa/020.JPG",
            'auteur': "Wuri",
            'date': "21-04-2024",
            'ville': "Abidjan",
            'contenu': "<p>Abidjan, le 07 mai 2024 – A l’occasion d’un atelier sur la revue du Projet d’identification unique pour l’intégration régionale de l’inclusion en Afrique de l’Ouest (WURI), le 06 mai 2024 à Abidjan, la directrice pays de la Banque mondiale pour la Côte d’Ivoire, le Bénin, la Guinée et le Togo, Marie Chantal Uwanyiligira, a indiqué que le projet WURI ambitionne de donner un identifiant à plus de 100 millions de personnes dans l’espace CEDEAO.</p> <p>« La CEDEAO compte à peu près 330 millions de personnes et parmi eux, 196 millions n’ont pas d’identifiant, ce qui veut dire qu’ils ne sont pas connus de leur gouvernement. Le projet WURI a pour ambition de donner un identifiant à plus de 100 millions de personnes », a déclaré Marie Chantal Uwanyiligira.</p> <p>Selon elle, le projet WURI vise à transformer positivement la vie des populations et permettre aux gouvernements de planifier le développement des pays. Et d’assurer que la Banque mondiale ne lésinera pas sur ses moyens pour permettre à ces personnes d’obtenir des documents d’identité.</p> <p>Pour le ministre de l’Emploi et de la Protection sociale, Adama Kamara, le projet WURI est en cohérence avec la vision du Président Alassane Ouattara qui a décidé de faire de la protection sociale un levier important de son développement économique.</p> <p>L’identifiant unique, de l’avis du ministre, permettra aux populations d’avoir accès, outre à la nationalité, aux services sociaux de base, notamment, les services de développement du capital humain, l’inclusion financière et économique.</p> <p>Il a rappelé que la Côte d’Ivoire a réussi, à fin 2023, à enrôler biométriquement plus de 10 millions des résidents grâce au programme WURI et vise l’identification de 20 millions de résidents fin 2024. </p> <p>Notons que cet atelier régional devrait permettre aux participants d’être situés sur l’état de mise en œuvre du projet WURI et de partager les expériences pour renforcer la coordination, nécessaire à l’interopérabilité régionale.</p>",
        },
        {
            'titre_court': 'Atelier regional du WURI',
            'titre_long': "Identification biométrique dans l’espace CEDEAO : plus de 100 millions de personnes visées par le projet WURI",
            'image': "img/melsa/020.JPG",
            'auteur': "Wuri",
            'date': "21-04-2024",
            'ville': "Abidjan",
            'contenu': "<p>Abidjan, le 07 mai 2024 – A l’occasion d’un atelier sur la revue du Projet d’identification unique pour l’intégration régionale de l’inclusion en Afrique de l’Ouest (WURI), le 06 mai 2024 à Abidjan, la directrice pays de la Banque mondiale pour la Côte d’Ivoire, le Bénin, la Guinée et le Togo, Marie Chantal Uwanyiligira, a indiqué que le projet WURI ambitionne de donner un identifiant à plus de 100 millions de personnes dans l’espace CEDEAO.</p> <p>« La CEDEAO compte à peu près 330 millions de personnes et parmi eux, 196 millions n’ont pas d’identifiant, ce qui veut dire qu’ils ne sont pas connus de leur gouvernement. Le projet WURI a pour ambition de donner un identifiant à plus de 100 millions de personnes », a déclaré Marie Chantal Uwanyiligira.</p> <p>Selon elle, le projet WURI vise à transformer positivement la vie des populations et permettre aux gouvernements de planifier le développement des pays. Et d’assurer que la Banque mondiale ne lésinera pas sur ses moyens pour permettre à ces personnes d’obtenir des documents d’identité.</p> <p>Pour le ministre de l’Emploi et de la Protection sociale, Adama Kamara, le projet WURI est en cohérence avec la vision du Président Alassane Ouattara qui a décidé de faire de la protection sociale un levier important de son développement économique.</p> <p>L’identifiant unique, de l’avis du ministre, permettra aux populations d’avoir accès, outre à la nationalité, aux services sociaux de base, notamment, les services de développement du capital humain, l’inclusion financière et économique.</p> <p>Il a rappelé que la Côte d’Ivoire a réussi, à fin 2023, à enrôler biométriquement plus de 10 millions des résidents grâce au programme WURI et vise l’identification de 20 millions de résidents fin 2024. </p> <p>Notons que cet atelier régional devrait permettre aux participants d’être situés sur l’état de mise en œuvre du projet WURI et de partager les expériences pour renforcer la coordination, nécessaire à l’interopérabilité régionale.</p>",
        },
        {
            'titre_court': 'Atelier regional du WURI',
            'titre_long': "Identification biométrique dans l’espace CEDEAO : plus de 100 millions de personnes visées par le projet WURI",
            'image': "img/melsa/020.JPG",
            'auteur': "Wuri",
            'date': "21-04-2024",
            'ville': "Abidjan",
            'contenu': "<p>Abidjan, le 07 mai 2024 – A l’occasion d’un atelier sur la revue du Projet d’identification unique pour l’intégration régionale de l’inclusion en Afrique de l’Ouest (WURI), le 06 mai 2024 à Abidjan, la directrice pays de la Banque mondiale pour la Côte d’Ivoire, le Bénin, la Guinée et le Togo, Marie Chantal Uwanyiligira, a indiqué que le projet WURI ambitionne de donner un identifiant à plus de 100 millions de personnes dans l’espace CEDEAO.</p> <p>« La CEDEAO compte à peu près 330 millions de personnes et parmi eux, 196 millions n’ont pas d’identifiant, ce qui veut dire qu’ils ne sont pas connus de leur gouvernement. Le projet WURI a pour ambition de donner un identifiant à plus de 100 millions de personnes », a déclaré Marie Chantal Uwanyiligira.</p> <p>Selon elle, le projet WURI vise à transformer positivement la vie des populations et permettre aux gouvernements de planifier le développement des pays. Et d’assurer que la Banque mondiale ne lésinera pas sur ses moyens pour permettre à ces personnes d’obtenir des documents d’identité.</p> <p>Pour le ministre de l’Emploi et de la Protection sociale, Adama Kamara, le projet WURI est en cohérence avec la vision du Président Alassane Ouattara qui a décidé de faire de la protection sociale un levier important de son développement économique.</p> <p>L’identifiant unique, de l’avis du ministre, permettra aux populations d’avoir accès, outre à la nationalité, aux services sociaux de base, notamment, les services de développement du capital humain, l’inclusion financière et économique.</p> <p>Il a rappelé que la Côte d’Ivoire a réussi, à fin 2023, à enrôler biométriquement plus de 10 millions des résidents grâce au programme WURI et vise l’identification de 20 millions de résidents fin 2024. </p> <p>Notons que cet atelier régional devrait permettre aux participants d’être situés sur l’état de mise en œuvre du projet WURI et de partager les expériences pour renforcer la coordination, nécessaire à l’interopérabilité régionale.</p>",
        }
    ]

    paginator = Paginator(actualites, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'actualites/index.html', {"page_obj": page_obj}) 


def home(request):
    articles = Post.objects.all()
    context = {"articles": articles }

    return render(request, 'actualites/home.html', context)
 

class  PostList(generic.ListView):
    queryset = Post.objects.filter(statut=1).order_by('-created_on')
    template_name = 'index.html'

#class DetailView(generic.DetailView):
#    model = Post
#    template_name = 'actualites/post_details.html'

def detail(request, id):
    article = get_object_or_404(Post, pk=id)
    return render(request, "actualites/post_details.html", {"article": article})
