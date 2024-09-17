from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    url = models.URLField(max_length=200,null=True)

    def __str__(self):
        return self.name
class Playlists(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    #inhalte = models.ManyToManyField("Quelle", on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Anwendung(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name
class Kategorien(models.Model):
    name = models.CharField(max_length=200)
    anwendung = models.ForeignKey(Anwendung, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name
class SubKategorien(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name
class Quelle(models.Model):
#    author = models.ForeignKey(Autor, on_delete=models.CASCADE,default="none", null=True)
    list = models.ForeignKey('Playlists', on_delete=models.CASCADE,default="none",null=True)
    kate = models.ForeignKey('Kategorien', on_delete=models.CASCADE,default="none",null=True)
    subkat = models.ForeignKey('SubKategorien', on_delete=models.CASCADE,default="none",null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    playlist_number = models.IntegerField(default=0,null=True)
    href = models.URLField(max_length=200)
    def __str__(self):
        return self.name