from django.urls import path


from . import views
app_name = 'linksammlung'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path("<int:quelle_id>/", views.quelle, name="quelle"),
    # ex: /polls/5/results/
    #path("<int:quelle_id>/subkategorien/", views.subkategorien, name="subkategorien"),
    # ex: /polls/5/vote/
    #path("<int:quelle_id>/kategorien/", views.kategorien, name="kategorien"),
    #path("<int:quelle_id>/autor/", views.autor, name="autor"),
    # ex: /polls/5/vote/
    #path("<int:quelle_id>/playlists/", views.playlists, name="playlists"),
    #path("<int:quelle_id>/anwendung/", views.anwendung, name="anwendung"),
]