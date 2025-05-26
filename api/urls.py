from django.urls import path
from .views import ProcessarView, StatusView

urlpatterns = [
    path('processar/', ProcessarView.as_view(), name='processar'),
    path('status/<int:pk>/', StatusView.as_view(), name='status'),
]
