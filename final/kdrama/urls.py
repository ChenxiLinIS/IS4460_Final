from django.urls import path
from . import views

urlpatterns = [

    path('kdrama_list/', views.KdramaList.as_view(), name='kdrama-list'),
    path('kdrama_details/<int:kdrama_id>/', views.KdramaDetails.as_view(), name='kdrama_details'),
    path('kdrama_add/', views.KdramaAdd.as_view(), name='kdrama_add'),
    path('kdrama_update/<int:kdrama_id>/', views.KdramaUpdate.as_view(), name='kdrama_update'),
    path('kdrama_delete/<int:kdrama_id>/', views.KdramaDelete.as_view(), name='kdrama_delete'),

    path('character_list/', views.CharacterList.as_view(), name='character-list'),
    path('character_details/<int:character_id>/', views.CharacterDetails.as_view(), name='character_details'),
    path('character_add/', views.CharacterAdd.as_view(), name='character_add'),
    path('character_update/<int:character_id>/', views.CharacterUpdate.as_view(), name='character_update'),
    path('character_delete/<int:character_id>/', views.CharacterDelete.as_view(), name='character_delete'),

    path('actor_list/', views.ActorList.as_view(), name='actor-list'),
    path('actor_details/<int:actor_id>/', views.ActorDetails.as_view(), name='actor_details'),
    path('actor_add/', views.ActorAdd.as_view(), name='actor_add'),
    path('actor_update/<int:actor_id>/', views.ActorUpdate.as_view(), name='actor_update'),
    path('actor_delete/<int:kdrama_id>/', views.ActorDelete.as_view(), name='actor_delete'),

    path('director_list/', views.DirectorList.as_view(), name='director-list'),
    path('director_details/<int:director_id>/', views.DirectorDetails.as_view(), name='director_details'),
    path('director_add/', views.DirectorAdd.as_view(), name='director_add'),
    path('director_update/<int:director_id>/', views.DirectorUpdate.as_view(), name='director_update'),
    path('director_delete/<int:director_id>/', views.DirectorDelete.as_view(), name='director_delete'),

    path('prodcompany_list/', views.ProdCompanyList.as_view(), name='prodcompany-list'),
    path('prodcompany_details/<int:prod_company_id>/', views.ProdCompanyDetails.as_view(), name='prodcompany_details'),
    path('prodcompany_add/', views.ProdCompanyAdd.as_view(), name='prodcompany_add'),
    path('prodcompany_update/<int:prod_company_id>/', views.ProdCompanyUpdate.as_view(), name='prodcompany_update'),
    path('prodcompany_delete/<int:prod_company_id>/', views.ProdCompanyDelete.as_view(), name='prodcompany_delete'),

    path('award_list/', views.AwardList.as_view(), name='award-list'),
    path('award_details/<int:award_id>/', views.AwardDetails.as_view(), name='award_details'),
    path('award_add/', views.AwardAdd.as_view(), name='award_add'),
    path('award_update/<int:award_id>/', views.AwardUpdate.as_view(), name='award_update'),
    path('award_delete/<int:award_id>/', views.AwardDelete.as_view(), name='award_delete'),

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
