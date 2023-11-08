from rest_framework import serializers
from .models import PaperTemplate


class PaperTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperTemplate
        fields = '__all__'