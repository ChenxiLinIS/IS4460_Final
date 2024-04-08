from django.urls import path
from . import views

urlpatterns = [
    path('kdrama/', views.KdramaListCreateView.as_view(), name = 'kdrama-list-create'),
    path('kdrama/<int:pk>/', views.KdramaDetailView.as_view(), name='kdrama-detail'),
    path('character/', views.CharacterListCreateView.as_view(), name = 'character-list-create'),
    path('character/<int:pk>/', views.CharacterDetailView.as_view(), name='character-detail'),
    path('actor/', views.ActorListCreateView.as_view(), name = 'actor-list-create'),
    path('actor/<int:pk>/', views.ActorDetailView.as_view(), name='actor-detail'),
    path('director/', views.DirectorListCreateView.as_view(), name = 'director-list-create'),
    path('director/<int:pk>/', views.DirectorDetailView.as_view(), name='director-detail'),
    path('prod_company/', views.ProdCompanyListCreateView.as_view(), name = 'prodcompany-list-create'),
    path('prod_company/<int:pk>/', views.ProdCompanyDetailView.as_view(), name='prodcompany-detail'),
    path('award/', views.AwardListCreateView.as_view(), name = 'award-list-create'),
    path('award/<int:pk>/', views.AwardDetailView.as_view(), name='award-detail'),
]
