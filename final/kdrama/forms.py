from django import forms
from django.core.validators import MaxValueValidator
from .models import kdrama, character, actor, director, prod_company, award

class KdramaForm(forms.ModelForm):
    class Meta:
        model = kdrama
        fields = '__all__'

class CharacterForm(forms.ModelForm):
    class Meta:
        model = character
        fields = '__all__'

class ActorForm(forms.ModelForm):
    class Meta:
        model = actor
        fields = '__all__'

class DirectorForm(forms.ModelForm):
    class Meta:
        model = director
        fields = '__all__'

class ProdCompanyForm(forms.ModelForm):
    class Meta:
        model = prod_company
        fields = '__all__'

class AwardForm(forms.ModelForm):
    class Meta:
        model = award
        fields = '__all__'

        
