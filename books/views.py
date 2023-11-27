from django.shortcuts import render
from .models import Books
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import BooksForm


def index(request):
    return render(request,"index.html")

def pilealire(request):
    data = Books.objects.all()
    context = {
        'data' : data
    }
    return render(request, "pilealire.html", {'Books': Books.objects.all()})


def view_book(request):
    id = request.GET.get('id','')

    books = Books.objects.get(pk=id)
    return HttpResponseRedirect(reverse('pilealire'))

def ajout(request):
    if request.method == 'POST' :

        new_book = Books(
            titre_livre =  request.POST['titre_livre'],
            nom_auteurice = request.POST['nom_auteurice'],
            prenom_auteurice =  request.POST['prenom_auteurice'],
            couverture=request.POST["couverture"])

        new_book.save()
        return render(request, 'ajout.html', {
            'form' : BooksForm(),
            'success' : True
            })

    print('else')
    return render(request, 'ajout.html', {'form' : BooksForm() })


def edit(request, id):
    if request.method == 'POST':
        books = Books.objects.get(pk=id)

        books.titre_livre =  request.POST['titre_livre']
        books.nom_auteurice = request.POST['nom_auteurice']
        books.prenom_auteurice =  request.POST['prenom_auteurice']
        books.couverture=request.POST["couverture"]
        books.save()
        
        return render(request, 'edit.html', {
        'form': BooksForm(),
        'success' : True
            })
    else:
        books = Books.objects.get(pk=id)
        form = BooksForm(instance=Books)
    return render(request, 'edit.html', {
        'form': form
    })    

