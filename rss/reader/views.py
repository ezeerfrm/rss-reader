from django.shortcuts import render, HttpResponse

from .forms import *

from .update import*
# Create your views here.



def add_rss(request):

    form_add_rss = add_rss_form(request.POST or None)

    if form_add_rss.is_valid():
        form_add_rss.save()
    return render(request, "add_rss.html", locals())

def update_rss(request):
    recup()
    return HttpResponse("update_rss")