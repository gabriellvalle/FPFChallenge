from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Calculator
from decimal import Decimal

class CalculatorTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_case_default(self):
        payload = {'num1': 10, 'num2': 20, 'num3': 30}
        post_response = self.client.post('/processar/', payload, format='json')
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)

        req_id = post_response.data['id']
        request = Calculator.objects.get(id=req_id)

        request.media = Decimal("20.00")
        request.mediana = Decimal("20.00")
        request.status = "Concluído"
        request.save()

        response = self.client.get(f'/status/{req_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], "Concluído")
        self.assertEqual(float(response.data['media']), 20.00)
        self.assertEqual(float(response.data['mediana']), 20.00)

    def test_case_missing(self):
        payload = {'num1': 10, 'num2': 20}
        response = self.client.post('/processar/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('num3', response.data)

    def test_case_invalid(self):
        payload = {'num1': "dez", 'num2': 20, 'num3': 30}
        response = self.client.post('/processar/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('num1', response.data)
