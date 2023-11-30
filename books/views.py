from django.shortcuts import render
from .models import Books
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import BooksForm


def index(request):
    return render(request,"index.html")

def pilealire(request):
    data = Books.objects.all()
    return render(request, "pilealire.html", {'Books': Books.objects.all()})


def view_book(request):
    id = request.GET.get('id','')

    books = Books.objects.get(pk=id)
    return HttpResponseRedirect(reverse('pilealire'))

def ajout(request):
    if request.method == 'POST' :

        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():

            new_book = Books(
                titre_livre = form.cleaned_data.get('titre_livre'),
                nom_auteurice = form.cleaned_data.get('nom_auteurice'),
                prenom_auteurice =  form.cleaned_data.get('prenom_auteurice'),
                couverture= form.cleaned_data.get('couverture'))

            new_book.save()
        
        else:
            print("Form was not valid!")
        
        return render(request, 'ajout.html', {
            'form' : BooksForm(),
            'success' : True
            })

    return render(request, 'ajout.html', {'form' : BooksForm() })


def edit(request, id):
    book = Books.objects.get(pk=id)

    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES, instance=book)

        if form.is_valid():

            book.titre_livre = request.POST['titre_livre']
            book.nom_auteurice = request.POST['nom_auteurice']
            book.prenom_auteurice =  request.POST['prenom_auteurice']
            new_couverture = request.POST['couverture'] 
            if new_couverture:
                book.couverture = new_couverture

            book.save()
            return render(request, 'edit.html', {'form' : form, 'success' : True })
    else:
        form = BooksForm(instance=book)
        return render(request, 'edit.html', {'form' : form })
             

def delete(request, id):
    if request.method == "POST":
           book = Books.objects.get(pk=id)
           book.delete()
    return HttpResponseRedirect(reverse('pilalire'))