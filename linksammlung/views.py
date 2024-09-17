from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView

from .models import Autor, Playlists, Kategorien, SubKategorien, Quelle, Anwendung
# Create your views here.

class IndexView(generic.ListView):
    #akt_Liste = Quelle.objects.order_by('-name')
    #templDS = Quelle.objects.get(pk=1)
    template_name = "index.html"
    context_object_name = "akt_Liste"
    def get_queryset(self):
        return Quelle.objects.all()




