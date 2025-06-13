from django.urls import path

from apps.notcoin.models import Balance
from apps.notcoin.views import ClickerView

urlpatterns = [
    path('', ClickerView.as_view(), name="clicker")
]
