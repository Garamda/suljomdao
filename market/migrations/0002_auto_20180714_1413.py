# Generated by Django 2.0.7 on 2018-07-14 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='price',
            field=models.CharField(max_length=100, verbose_name='ETH 가격'),
        ),
    ]
