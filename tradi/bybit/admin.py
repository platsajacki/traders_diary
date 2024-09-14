from django.contrib import admin
from django.http.request import HttpRequest

from bybit.models import Kline


@admin.register(Kline)
class KlineAdmin(admin.ModelAdmin):
    """
    Админская модель для управления ценовыми барами (Kline).
    """

    list_display = (
        'pair',
        'interval',
        'start_time',
        'open_price',
        'high_price',
        'low_price',
        'close_price',
        'volume',
        'turnover',
    )
    list_filter = ('pair', 'interval', 'start_time')
    search_fields = ('pair__symbol',)
    ordering = ('pair__base_asset', '-start_time')
    readonly_fields = (
        'pair',
        'interval',
        'start_time',
        'open_price',
        'high_price',
        'low_price',
        'close_price',
        'volume',
        'turnover',
    )

    def has_add_permission(self, request: HttpRequest) -> bool:
        """
        Запрещает добавление новых объектов Kline в админке.
        """
        return False

    def has_change_permission(self, request: HttpRequest, obj: Kline | None = None) -> bool:
        """
        Запрещает изменение существующих объектов Kline в админке.
        """
        return False

    def has_delete_permission(self, request: HttpRequest, obj: Kline | None = None) -> bool:
        """
        Запрещает удаление существующих объектов Kline в админке.
        """
        return False
