from django.forms import forms ,ModelForm, ModelChoiceField
from .models import *
from django.db.models.functions import Lower

class label_add_rss_form(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nom



class add_rss_form(ModelForm):

    categorie =  label_add_rss_form(Categorie.objects.all().order_by(Lower('nom')))

    class Meta:
         model = Rss_a_suivre
         fields = '__all__'