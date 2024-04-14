from rest_framework import serializers
from .models import kdrama, character, actor, director, prod_company, award, Purchase

class KdramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = kdrama
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = character
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = director
        fields = '__all__'

class ProdCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = prod_company
        fields = '__all__'

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = award
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'