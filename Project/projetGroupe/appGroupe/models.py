from django.db import models

class Personne(models.Model):
    Genre = (('M', ('Masculin')), 
('F', ('Feminin')), 
('Autre', ('Autre')), 
)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    genre = models.CharField(max_length=32, choices=Genre)
    naissance = models.DateTimeField('date de naisssance') 
    nationnalite=models.CharField(max_length=50)
    def __str__(self):
        return self.nom
    
class Adresse(models.Model):
    telephone = models.CharField(max_length=20,blank=True,unique=True) 
    email = models.EmailField(max_length=250,unique=True)
    quartier = models.CharField(max_length=150) 
    ville = models.CharField(max_length=150)
    def __str__(self): 
        return self.email

class Dossier(models.Model):
    numero_dossier=models.CharField(max_length=30)
    lettreMotivation=models.FileField(upload_to="document",blank=True) 
    releverDeNote=models.FileField(upload_to="document",blank=True)
    def __str__(self): 
        return self.numero_dosier

    
class Bachelier(Personne):
    adresse=models.ForeignKey(Adresse,on_delete=models.CASCADE)
    dossier=models.ManyToManyField(Dossier)
    def __str__(self): 
        return self.nom

class Conseiller_orientation(Personne):
    Grade=(('li',('licence')),
           ('ma',('Master')),
           ('do',('Docteorat')),)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    grade=models.CharField(max_length=20,choices=Grade)
    def __str__(self):
        return self.adresse
    
class EntiteRessource(models.Model):
    nom=models.CharField(max_length=20)
    adresse=models.ForeignKey(Adresse,on_delete=models.CASCADE)
    def __str__(self): 
       return self.adresse




# Create your models here.

# Create your models here.
