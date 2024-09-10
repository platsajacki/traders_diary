from django.db import models

from core.models import NameStringMethod, TimestampedModel


class AssetType(models.TextChoices):
    STOCK = 'ST', 'Акция'
    CURRENCY = 'CR', 'Валюта'
    CRYPTOCURRENCY = 'CC', 'Криптовалюта'


class Exchange(NameStringMethod):
    name = models.CharField(
        'Название',
    )

    class Meta:
        verbose_name = 'Биржа'
        verbose_name_plural = 'Биржи'


class FinancialAsset(TimestampedModel):
    ticker = models.CharField(
        'Тикер',
        max_length=50,
    )
    traded = models.BooleanField(
        'Торгуемый',
    )
    type = models.CharField(
        'Тип актива',
        max_length=2,
        choices=AssetType.choices,
    )
    exchanges = models.ManyToManyField(
        Exchange,
        related_name='assets',
        verbose_name='Биржи',
    )

    def __str__(self) -> str:
        return f'{self.type} - {self.ticker}'

    class Meta:
        verbose_name = 'Финансовый актив'
        verbose_name_plural = 'Финансовые активы'
