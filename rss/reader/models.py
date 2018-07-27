from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length = 1000, default = '')

class Rss_a_suivre(models.Model):
    nom = models.CharField(max_length = 1000)
    lien = models.URLField(max_length=1000)
    categorie =models.ForeignKey('Categorie', on_delete=models.CASCADE,)

class Articles  (models.Model):
    origine = models.ForeignKey('Rss_a_suivre', on_delete=models.CASCADE,)
    title = models.CharField(max_length = 1000)
    pubDate = models.DateField()
    description = models.TextField()
    content = models.TextField(blank = True, null = True)
    starred = models.BooleanField(default = False)
    lu  = models.BooleanField(default = False)
    lien = models.URLField(default ='',max_length=1000)