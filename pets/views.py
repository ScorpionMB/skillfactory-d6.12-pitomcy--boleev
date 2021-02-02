# from django.shortcuts import redirect, render
from .models import Pet
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView


class IndexPageView(TemplateView):

    template_name = 'pets/index.html'

class ContactsView(TemplateView):

    template_name = 'pets/contacts.html'

class PetListView(ListView):
    
    model = Pet  
    template_name = 'pets/pet_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()

        # search
        if get_params.get('q'):
            qs = qs.filter(name__icontains=get_params.get('q'))

        # filter
        if get_params.get('filter'):
            qs = qs.filter(type_of_animal=get_params.get('filter'))
        
        # all
        if get_params.get('all'):
            qs = qs.all
        return qs   

class PetView(DetailView):
    
    model = Pet