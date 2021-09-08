# Generated by Django 3.1.4 on 2021-09-08 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(verbose_name='Дата поступления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='provider',
            field=models.CharField(blank=True, max_length=256, verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.IntegerField(choices=[(1, 'шт.'), (2, 'кг.')], verbose_name='Единица измерения'),
        ),
    ]