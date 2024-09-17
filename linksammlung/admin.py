from django.contrib import admin

# Register your models here.
from .models import Autor, Playlists, Kategorien, SubKategorien, Quelle, Anwendung
admin.site.register(Autor)
admin.site.register(Playlists)
admin.site.register(Kategorien)
admin.site.register(SubKategorien)
admin.site.register(Quelle)
admin.site.register(Anwendung)
