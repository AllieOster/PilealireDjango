from django import forms
from .models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['titre_livre', 'nom_auteurice', 'prenom_auteurice', 'couverture']
        labels = {
        'titre_livre' : "titre du livre  ",
        'nom_auteurice' : "Nom de l'auteurice  ",
        'prenom_auteurice' : "prénom de l'auteurice  ",
        'couverture' : "Couverture "
        }
        widgets = {'titre_livre' : forms.TextInput(attrs={'class': 'form-control'}), 
                   'nom_auteurice' : forms.TextInput(attrs={'class': 'form-control'}),
                    'prenom_auteurice' : forms.TextInput(attrs={'class': 'form-control'}), 
                    'couverture' : forms.ClearableFileInput(attrs={'class': 'form-control'})
                    }

