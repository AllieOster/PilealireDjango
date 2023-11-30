from django.urls import path
from .import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('pilealire', views.pilealire, name='pilealire'),
    path('ajout', views.ajout, name='ajout'),
    path('view_book', views.view_book, name='view_book'),
    # path('add/', views.add, name='add')
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete')
]
