from typing import Any

from django.db import models

from core.models import TimestampedModel

from tradi.accounting.models.finances import TradingPair


class Kline(TimestampedModel):
    pair = models.ForeignKey(
        TradingPair,
        on_delete=models.CASCADE,
        verbose_name='Торговая пара',
        related_name='Klines',
    )
