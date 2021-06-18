from source.models import Source, SourceKind, Price, Province 
from rest_framework import viewsets
from source.serializers import SourceKindSerializer, SourceSerializer, PriceSerializer, ProvinceSerializer 

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer 


class SourceKindViewSet(viewsets.ModelViewSet):
    queryset = SourceKind.objects.all()
    serializer_class = SourceKindSerializer 


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer 


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer 
