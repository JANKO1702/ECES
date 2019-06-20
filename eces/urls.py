from django.urls import path
#from site_django.views import acceuil, etudiant, EtudiantListView
from . import views
from .views import Detail

urlpatterns = [
    path('',views.acceuil, name='acceuil'),
    path('etudiant/',views.etudiant, name='etudiant'),
    path('detail/<int:pk>',Detail.as_view(), name='detail'),
    #path('liste_etudiant/', EtudiantListView.as_view(), name='liste_etudiant'),
]
