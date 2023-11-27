from django.db import models

class Books(models.Model):
    titre_livre = models.CharField(max_length=150)
    nom_auteurice = models.CharField(max_length=50)
    prenom_auteurice = models.CharField(max_length=50)
    couverture = models.ImageField(upload_to='pics')

    def __str__(self):
        return f'Books:{self.titre_livre} {self.nom_auteurice} {self.prenom_auteurice} {self.couverture}'

