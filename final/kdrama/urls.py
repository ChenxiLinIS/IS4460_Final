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
 