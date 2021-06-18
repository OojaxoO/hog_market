from rest_framework import serializers
from source.models import Source, SourceKind, Price, Province 


class SourceKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceKind 
        fields = "__all__"
        

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source 
        fields = "__all__"


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province 
        fields = "__all__"


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price 
        fields = "__all__"