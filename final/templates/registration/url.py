from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # URL for the login page
    path('kdrama_list/', views.kdrama_list, name='kdrama_list'),  # URL for kdrama list page
]
