from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError

class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'
    
    def validate_fayl(self, qimat):
        if not qimat.url.endswith('.mp3'):
            raise ValidationError('Xato')
        return qimat
    
class QoshiqchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'

class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'