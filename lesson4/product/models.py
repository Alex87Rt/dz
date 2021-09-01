from django.db import models


class Product(models.Model):
    UNITS = (
        (1, 'шт.'),
        (2, 'ед.'),
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(verbose_name='Наименоваие', max_length=128)
    date = models.DateField(verbose_name='Дата прихода')
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=0, default=0)
    unit = models.IntegerField(verbose_name='Единица измерения', choices=UNITS)
    provider = models.CharField(verbose_name='Поставщик', max_length=256, blank=True)
