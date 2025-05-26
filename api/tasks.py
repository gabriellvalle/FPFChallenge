from celery import shared_task
from .models import Calculator
from decimal import Decimal, ROUND_HALF_UP

@shared_task
def processar_calculo(request_id):
    try:
        req = Calculator.objects.get(id=request_id)
        numeros = sorted([req.num1, req.num2, req.num3])
        media = Decimal(sum(numeros) / 3).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        mediana = Decimal(numeros[1]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        req.media = media
        req.mediana = mediana
        req.status = "Concluído"
        req.save()
    except Calculator.DoesNotExist:
        pass
