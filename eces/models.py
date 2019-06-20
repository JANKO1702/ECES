from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    matricule = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10)
    option = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)
    télephone = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.nom.title()
