# from typing import Any

from django.db import models

from accounting.models.finances import TradingPair
from core.models import TimestampedModel


class Kline(TimestampedModel):
    pair = models.ForeignKey(
        TradingPair,
        on_delete=models.CASCADE,
        verbose_name='Торговая пара',
        related_name='Klines',
    )
