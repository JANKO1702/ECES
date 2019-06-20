from django.shortcuts import render
from django.views.generic import DetailView
from .models import Etudiant
#from django.http import HttpResponse

# Create your views here.
def acceuil(request):
    return render(request,"pages/acceuil.html")

def etudiant(request):
    liste = Etudiant.objects.all()
    return render(request,"pages/etudiant.html", {'liste':liste})


def detail(request):
    regarder=Etudiant.objects.get(pk=id)
    return render (request, "pages/detail.html", {'regarder':regarder})

class Detail(DetailView):
    model = Etudiant
    template_name = "pages/detail.html"
#class EtudiantListView(ListView):
#    template_name = "site_django/liste.html"
