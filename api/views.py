from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Calculator
from .serializers import CalculatorSerializer
from django.shortcuts import get_object_or_404
from .tasks import processar_calculo

class ProcessarView(APIView):
    def post(self, request):
        serializer = CalculatorSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            processar_calculo.delay(instance.id)
            return Response({'id': instance.id, 'status': instance.status}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusView(APIView):
    def get(self, request, pk):
        instance = get_object_or_404(Calculator, pk=pk)
        serializer = CalculatorSerializer(instance)
        return Response(serializer.data)
