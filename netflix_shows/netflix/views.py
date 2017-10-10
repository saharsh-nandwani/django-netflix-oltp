from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from. serializers import (NetflixSerializers)

from. models import Netflix

class NetflixViewSet(ModelViewSet):
    serializer_class = NetflixSerializers
    queryset = Netflix.objects.all()
