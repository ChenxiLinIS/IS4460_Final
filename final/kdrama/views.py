from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import kdrama, character, actor, director, prod_company, award, Purchase
from .forms import KdramaForm, CharacterForm, ActorForm, DirectorForm, ProdCompanyForm, AwardForm
from rest_framework import generics
from .serializers import KdramaSerializer, CharacterSerializer, ActorSerializer, DirectorSerializer, ProdCompanySerializer, AwardSerializer, PurchaseSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def can_modify_information(request):
    return request.user.groups.filter(name='Admin').exists()

def user_purchase(request):
    return request.user.groups.filter(name='User').exists()
    

class KdramaList(LoginRequiredMixin, View):
    def get(self, request):
        user_can_modify = can_modify_information(request)
        user_can_purchase = user_purchase(request)
        kdramas = kdrama.objects.all()
        return render(request=request, template_name='kdrama/kdrama_list.html', context={'kdramas': kdramas, 'user_can_modify': user_can_modify, 'user_can_purchase': user_can_purchase})

class KdramaDetails(LoginRequiredMixin, View):
    def get(self, request, kdrama_id):
        kdrama1 = get_object_or_404(kdrama, pk=kdrama_id)
        user_can_modify = can_modify_information(request)
        user_can_purchase = user_purchase(request)
        return render(request=request, template_name='kdrama/kdrama_details.html', context={'kdrama': kdrama1,'user_can_modify': user_can_modify, 'user_can_purchase': user_can_purchase})

    
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

class KdramaDelete(View):

    def get(self,request,kdrama_id=None):

        if kdrama_id:
            kdrama = kdrama.objects.get(pk=kdrama_id)
        else:
            kdrama = kdrama()

        form = KdramaForm(instance=kdrama)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'kdrama/kdrama_delete.html',context = {'kdrama':kdrama,'form':form})
      
    
    def post(self,request,kdrama_id=None):

        kdrama = kdrama.objects.get(pk=kdrama_id)

        form = KdramaForm(request.POST,instance=kdrama)

        kdrama.delete()

        return redirect(reverse("kdrama-list"))

class CharacterList(View):
    def get(self, request):
        characters = character.objects.all()
        return render(request=request, template_name='kdrama/character_list.html', context={'characters': characters})

class CharacterDetails(View):
    def get(self, request, character_id):
        character1 = get_object_or_404(character, pk=character_id)
        return render(request=request, template_name='kdrama/character_details.html', context={'character': character1})

    
class CharacterAdd(View):
    def get(self, request):

        form = CharacterForm()

        return render(request=request, template_name='kdrama/character_add.html', context={'form': form})

    def post(self, request):

        form = CharacterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('character-list') 
        
        return render(request=request, template_name='kdrama/character_add.html', context={'form': form})

class CharacterUpdate(View):

    def get(self, request, character_id):

        movie = get_object_or_404(character, pk=character_id)

        form = CharacterForm(instance=character)

        return render(request=request, template_name='kdrama/character_update.html', context={'form': form, 'character': character})

    def post(self, request, character_id):

        character = get_object_or_404(character, pk=character_id)

        form = CharacterForm(request.POST, instance=character)

        if form.is_valid():
            form.save()
            return redirect('character-list')
        
        return render(request=request, template_name='kdrama/character_update.html', context={'form': form, 'character': character})

class CharacterDelete(View):

    def get(self,request,character_id=None):

        if character_id:
            character = character.objects.get(pk=character_id)
        else:
            character = character()

        form = CharacterForm(instance=character)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'kdrama/character_delete.html',context = {'character':character,'form':form})
      
    
    def post(self,request,character_id=None):

        character = character.objects.get(pk=character_id)

        form = CharacterForm(request.POST,instance=character)

        character.delete()

        return redirect(reverse("character-list"))


class ActorList(View):
    def get(self, request):
        actors = actor.objects.all()
        return render(request=request, template_name='kdrama/actor_list.html', context={'actors': actors})

class ActorDetails(View):
    def get(self, request, actor_id):
        actor1 = get_object_or_404(actor, pk=actor_id)
        return render(request=request, template_name='kdrama/actor_details.html', context={'actor': actor1})

    
class ActorAdd(View):
    def get(self, request):

        form = ActorForm()

        return render(request=request, template_name='kdrama/actor_add.html', context={'form': form})

    def post(self, request):

        form = ActorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('actor-list') 
        
        return render(request=request, template_name='kdrama/actor_add.html', context={'form': form})

class ActorUpdate(View):

    def get(self, request, actor_id):

        actor1 = get_object_or_404(actor, pk=actor_id)

        form = ActorForm(instance=actor1)

        return render(request=request, template_name='kdrama/actor_update.html', context={'form': form, 'actor': actor1})

    def post(self, request, actor_id):

        actor = get_object_or_404(actor, pk=actor_id)

        form = ActorForm(request.POST, instance=actor)

        if form.is_valid():
            form.save()
            return redirect('actor-list')
        
        return render(request=request, template_name='kdrama/actor_update.html', context={'form': form, 'actor': actor})

class ActorDelete(View):

    def get(self,request,kdrama_id=None):
        actor1 = None
        if kdrama_id:
            actor1 = actor.objects.get(pk=kdrama_id)
        else:
            actor1 = actor()

        form = ActorForm(instance=actor)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'kdrama/actor_delete.html',context = {'actor':actor1,'form':form})
      
    
    def post(self,request,actor_id=None):

        actor1 = actor.objects.get(pk=actor_id)

        form = ActorForm(request.POST,instance=actor1)

        actor1.delete()

        return redirect(reverse("actor-list"))
    
class DirectorList(View):
    def get(self, request):
        directors = director.objects.all()
        return render(request=request, template_name='kdrama/director_list.html', context={'directors': directors})

class DirectorDetails(View):
    def get(self, request, director_id):
        directors = get_object_or_404(director, pk=director_id)
        return render(request=request, template_name='kdrama/director_details.html', context={'director': directors})

    
class DirectorAdd(View):
    def get(self, request):

        form = DirectorForm()

        return render(request=request, template_name='kdrama/director_add.html', context={'form': form})

    def post(self, request):

        form = DirectorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('director-list') 
        
        return render(request=request, template_name='kdrama/director_add.html', context={'form': form})

class DirectorUpdate(View):

    def get(self, request, director_id):

        directors = get_object_or_404(director, pk=director_id)

        form = DirectorForm(instance=directors)

        return render(request=request, template_name='kdrama/director_update.html', context={'form': form, 'director': directors})

    def post(self, request, director_id):

        directors = get_object_or_404(director, pk=director_id)

        form = DirectorForm(request.POST, instance=directors)

        if form.is_valid():
            form.save()
            return redirect('director-list')
        
        return render(request=request, template_name='kdrama/director_update.html', context={'form': form, 'director': directors})

class DirectorDelete(View):

    def get(self,request,director_id=None):

        if director_id:
            director1 = director.objects.get(pk=director_id)
        else:
            director1 = director()

        form = DirectorForm(instance=director)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'kdrama/director_delete.html',context = {'director':director1,'form':form})
      
    
    def post(self,request,director_id=None):

        director1 = director.objects.get(pk=director_id)

        form = DirectorForm(request.POST,instance=director)

        director.delete()

        return redirect(reverse("director-list"))

class ProdCompanyList(View):
    def get(self, request):
        prod_companies = prod_company.objects.all()
        return render(request=request, template_name='kdrama/prodcompany_list.html', context={'prod_companies': prod_companies})

class ProdCompanyDetails(View):
    def get(self, request, prod_company_id):
        prod_company1 = get_object_or_404(prod_company, pk=prod_company_id)
        return render(request=request, template_name='kdrama/prodcompany_details.html', context={'prod_company': prod_company1})

    
class ProdCompanyAdd(View):
    def get(self, request):

        form = ProdCompanyForm()

        return render(request=request, template_name='kdrama/prodcompany_add.html', context={'form': form})

    def post(self, request):

        form = ProdCompanyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('prodcompany-list') 
        
        return render(request=request, template_name='kdrama/prodcompany_add.html', context={'form': form})

class ProdCompanyUpdate(View):

    def get(self, request, prod_company_id):

        prod_company1 = get_object_or_404(prod_company, pk=prod_company_id)

        form = ProdCompanyForm(instance=prod_company1)

        return render(request=request, template_name='kdrama/prodcompany_update.html', context={'form': form, 'prod_company': prod_company1})

    def post(self, request, prod_company_id):

        prod_company = get_object_or_404(prod_company, pk=prod_company_id)

        form = ProdCompanyForm(request.POST, instance=prod_company)

        if form.is_valid():
            form.save()
            return redirect('prodcompany-list')
        
        return render(request=request, template_name='kdrama/prodcompany_update.html', context={'form': form, 'prod_company': prod_company})

class ProdCompanyDelete(View):

    def get(self,request,prod_company_id=None):

        if prod_company_id:
            prod_company1 = prod_company.objects.get(pk=prod_company_id)
        else:
            prod_company1 = prod_company()

        form = ProdCompanyForm(instance=prod_company1)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'kdrama/prodcompany_delete.html',context = {'prod_company':prod_company1,'form':form})
      
    
    def post(self,request,prod_company_id=None):

        prod_company = prod_company.objects.get(pk=prod_company_id)

        form = ProdCompanyForm(request.POST,instance=prod_company)

        prod_company.delete()

        return redirect(reverse("prodcompany-list"))

class AwardList(View):
    def get(self, request):
        awards = award.objects.all()
        return render(request=request, template_name='kdrama/award_list.html', context={'awards': awards})

class AwardDetails(View):
    def get(self, request, award_id):
        award1 = get_object_or_404(award, pk=award_id)
        return render(request=request, template_name='kdrama/award_details.html', context={'award': award1})

    
class AwardAdd(View):
    def get(self, request):

        form = AwardForm()

        return render(request=request, template_name='kdrama/award_add.html', context={'form': form})

    def post(self, request):

        form = AwardForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('award-list') 
        
        return render(request=request, template_name='kdrama/award_add.html', context={'form': form})

class AwardUpdate(View):

    def get(self, request, award_id):

        award1 = get_object_or_404(award, pk=award_id)

        form = AwardForm(instance=award1)

        return render(request=request, template_name='kdrama/award_update.html', context={'form': form, 'award': award1})

    def post(self, request, award_id):

        award = get_object_or_404(kdrama, pk=award_id)

        form = AwardForm(request.POST, instance=award)

        if form.is_valid():
            form.save()
            return redirect('award-list')
        
        return render(request=request, template_name='kdrama/award_update.html', context={'form': form, 'award': award})

class AwardDelete(View):

    def get(self,request,award_id=None):

        if award_id:
            award1 = award.objects.get(pk=award_id)
        else:
            award1 = award()

        form = AwardForm(instance=award1)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'kdrama/award_delete.html',context = {'award':award1,'form':form})
      
    
    def post(self,request,award_id=None):

        award = award.objects.get(pk=award_id)

        form = AwardForm(request.POST,instance=award)

        award.delete()

        return redirect(reverse("award-list"))

class PurchaseView(View):
    def get(self, request, kdrama_id):
        kdramas = kdrama.objects.get(pk=kdrama_id)
        return render(request, 'purchase.html', {'kdrama': kdramas})

    def post(self, request, kdrama_id):
        kdramas = kdrama.objects.get(pk=kdrama_id)
        purchase_amount = request.POST.get('purchase_amount')
        user_id = request.user 
        purchase = Purchase.objects.create(kdramas=kdrama, user_id=user_id, amount=purchase_amount)
        return render(request, 'purchase_complete.html', {'purchase': purchase})
    
class PurchaseCompleteView(View):
    def get(self, request):
        return render(request, 'purchase_complete.html')

class KdramaListCreateView(generics.ListCreateAPIView):

    queryset = kdrama.objects.all()
    serializer_class = KdramaSerializer

class KdramaDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = kdrama.objects.all()
    serializer_class = KdramaSerializer


class CharacterListCreateView(generics.ListCreateAPIView):

    queryset = character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = character.objects.all()
    serializer_class = CharacterSerializer

class ActorListCreateView(generics.ListCreateAPIView):

    queryset = actor.objects.all()
    serializer_class = ActorSerializer

class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = actor.objects.all()
    serializer_class = ActorSerializer

class DirectorListCreateView(generics.ListCreateAPIView):

    queryset = director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = director.objects.all()
    serializer_class = DirectorSerializer

class ProdCompanyListCreateView(generics.ListCreateAPIView):

    queryset = prod_company.objects.all()
    serializer_class = ProdCompanySerializer

class ProdCompanyDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = prod_company.objects.all()
    serializer_class = ProdCompanySerializer

class AwardListCreateView(generics.ListCreateAPIView):

    queryset = award.objects.all()
    serializer_class = AwardSerializer

class AwardDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = award.objects.all()
    serializer_class = AwardSerializer
#change

