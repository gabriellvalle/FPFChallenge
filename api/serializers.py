from rest_framework import serializers
from .models import Calculator

class CalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculator
        fields = '__all__'
        read_only_fields = ['status', 'media', 'mediana', 'created_at']
