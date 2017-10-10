from rest_framework import serializers
from .models import Netflix


class NetflixSerializers(serializers.ModelSerializer):
    class Meta:
        model = Netflix
        fields = ('name', 'rating', 'castName', 'genre', 'created_at', 'updated_at')
