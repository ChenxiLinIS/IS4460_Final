from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import kdrama, character, actor, director, prod_company, award
from rest_framework import generics
from .serializers import KdramaSerializer, CharacterSerializer, ActorSerializer, DirectorSerializer, ProdCompanySerializer, AwardSerializer

# Create your views here.

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