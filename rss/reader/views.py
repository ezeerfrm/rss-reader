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
    for i in Rss_a_suivre.objects.values('lien') : 
        print(i['lien'])
        recup(i['lien'])
    return HttpResponse("update_rss")

def lecture(request):
    articles = Articles.objects.all().order_by('origine', 'pubDate')
    return render(request, 'lecture.html', locals())
