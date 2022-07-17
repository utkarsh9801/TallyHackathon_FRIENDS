from rest_framework import serializers
from .models import ScoreModel


class scoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreModel
        fields = '__all__'
