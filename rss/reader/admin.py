from django.contrib import admin

# Register your models here.
from .models import Articles, Categorie, Rss_a_suivre

admin.site.register(Articles)
admin.site.register(Categorie)
admin.site.register(Rss_a_suivre)