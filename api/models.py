from django.db import models

class Calculator(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    num3 = models.FloatField()

    status = models.CharField(max_length=20, default='Processando')
    media = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    mediana = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Requisição #{self.id} - Status: {self.status}"
