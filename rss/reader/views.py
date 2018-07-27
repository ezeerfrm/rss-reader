from django.shortcuts import render, HttpResponse

from .forms import *
from .models import *
from .update import *
# Create your views here.



def add_rss(request):

    form_add_rss = add_rss_form(request.POST or None)

    if form_add_rss.is_valid():
        form_add_rss.save()
    return render(request, "add_rss.html", locals())

def update_rss(request):
    print(request.GET.get("token","pas de token"))
    if request.GET.get("token","pas de token") == '0Y.h8DwNExvvwpiivn':
        for i in Rss_a_suivre.objects.values('lien') : 
            print(i['lien'])
            recup(i['lien'])
        return HttpResponse("update_rss")
    else:
        return HttpResponse("wrong token")

def lecture(request):
    titre =  "Lecture"
    star=  request.GET.get("id_star", None)
    unstar=  request.GET.get("id_unstar", None)
    lu =  request.GET.get("id_lu", None)

    if star != None:
        obj = Articles.objects.get(lien = star)
        obj.starred = True
        obj.save()

    if unstar != None:
        obj = Articles.objects.get(lien = unstar)
        obj.starred = False
        obj.save()
    
    if lu != None:
        obj = Articles.objects.get(lien = lu)
        obj.lu = True
        obj.save()

    articles = Articles.objects.filter(lu = False).order_by('origine', 'pubDate')
    return render(request, 'lecture.html', locals())

def favoris(request):
    titre = "Favoris"
    articles = Articles.objects.filter(starred = True).order_by('origine', 'pubDate')
    return render(request, 'lecture.html', locals())