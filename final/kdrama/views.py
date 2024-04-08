from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import kdrama, character, actor, director, prod_company, award
from .forms import KdramaForm, CharacterForm, ActorForm, DirectorForm, ProdCompanyForm, AwardForm
from rest_framework import generics
from .serializers import KdramaSerializer, CharacterSerializer, ActorSerializer, DirectorSerializer, ProdCompanySerializer, AwardSerializer

# Create your views here.

class KdramaList(View):
    def get(self, request):
        kdramas = kdrama.objects.all()
        return render(request=request, template_name='kdrama/kdrama_list.html', context={'kdramas': kdramas})

class KdramaDetails(View):
    def get(self, request, kdrama_id):
        kdrama = get_object_or_404(kdrama, pk=kdrama_id)
        return render(request=request, template_name='kdrama/kdrama_details.html', context={'kdrama': kdrama})

    
class KdramaAdd(View):
    def get(self, request):

        form = KdramaForm()

        return render(request=request, template_name='kdrama/kdrama_add.html', context={'form': form})

    def post(self, request):

        form = KdramaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('kdrama-list') 
        
        return render(request=request, template_name='kdrama/kdrama_add.html', context={'form': form})

class KdramaUpdate(View):

    def get(self, request, kdrama_id):

        movie = get_object_or_404(kdrama, pk=kdrama_id)

        form = KdramaForm(instance=kdrama)

        return render(request=request, template_name='kdrama/kdrama_update.html', context={'form': form, 'kdrama': kdrama})

    def post(self, request, kdrama_id):

        kdrama = get_object_or_404(kdrama, pk=kdrama_id)

        form = KdramaForm(request.POST, instance=kdrama)

        if form.is_valid():
            form.save()
            return redirect('kdrama-list')
        
        return render(request=request, template_name='kdrama/kdrama_update.html', context={'form': form, 'kdrama': kdrama})

class KdramaDe