from django.db import models

from accounting.models.finances import TradingPair
from core.models import TimestampedModel


class TimeInterval(models.TextChoices):
    """Временной интервал"""

    MIN_1 = '1', '1 минута'
    MIN_3 = '3', '3 минуты'
    MIN_5 = '5', '5 минут'
    MIN_15 = '15', '15 минут'
    MIN_30 = '30', '30 минут'
    HOUR_1 = '60', '1 час'
    HOUR_2 = '120', '2 часа'
    HOUR_4 = '240', '4 часа'
    HOUR_6 = '360', '6 часов'
    HOUR_12 = '720', '12 часов'
    DAY_1 = 'D', '1 день'
    MONTH_1 = 'M', '1 месяц'
    WEEK_1 = 'W', '1 неделя'


class Kline(TimestampedModel):
    """
    Модель, представляющая ценовой бар (свечу) для заданной торговой пары на определенном временном интервале.

    Атрибуты:
        pair (ForeignKey): Торговая пара, к которой относится данный бар.
        interval (CharField): Временной интервал свечи (например, 1 минута, 1 день, 1 месяц).
        start_time (DateTimeField): Время начала формирования бара.
        open_price (DecimalField): Цена открытия бара.
        high_price (DecimalField): Наивысшая цена бара.
        low_price (DecimalField): Низшая цена бара.
        close_price (DecimalField): Цена закрытия бара, если свеча закрыта, либо последняя цена сделки.
        volume (DecimalField): Объем торгов за период свечи.
        turnover (DecimalField): Оборот торгов в квотируемых монетах за период свечи.
    """

    pair = models.ForeignKey(
        TradingPair,
        on_delete=models.CASCADE,
        verbose_name='Торговая пара',
        related_name='Klines',
        editable=False,
    )
    interval = models.CharField(
        max_length=3,
        choices=TimeInterval.choices,
        verbose_name='Интервал',
        editable=False,
    )
    start_time = models.DateTimeField(
        verbose_name='Время начала',
        editable=False,
    )
    open_price = models.DecimalField(
        max_digits=20,
        decimal_places=8,
        verbose_name='Цена открытия',
        editable=False,
    )
    high_price = models.DecimalField(
        max_digits=20,
        decimal_places=8,
        verbose_name='Наивысшая цена',
        editable=False,
    )
    low_price = models.DecimalField(
        max_digits=20,
        decimal_places=8,
        verbose_name='Низшая цена',
        editable=False,
    )
    close_price = models.DecimalField(
        max_digits=20,
        decimal_places=8,
        verbose_name='Цена закрытия',
        help_text='Это последняя цена сделки, если свеча не закрыта.',
        editable=False,
    )
    volume = models.DecimalField(
        max_digits=20,
        decimal_places=8,
        verbose_name='Объем',
        help_text='Для контрактов: количество контрактов. Для спотов: количество монет.',
        editable=False,
    )
    turnover = models.DecimalField(
        max_digits=20,
        decimal_places=8,
        verbose_name='Оборот',
        help_text='Единица измерения: количество квотируемых монет.',
        editable=False,
    )

    class Meta:
        verbose_name = 'Бар'
        verbose_name_plural = 'Бары'

    def __str__(self) -> str:
        return f'{self.pair.symbol} {self.interval}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.base_asset}, {self.quote_asset})'
