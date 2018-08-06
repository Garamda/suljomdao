# Generated by Django 2.0.7 on 2018-08-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_cat_fin_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='make_sul',
            name='market_img',
        ),
        migrations.AddField(
            model_name='make_sul',
            name='ingredient',
            field=models.CharField(default=1, max_length=250, verbose_name='재료들 id'),
            preserve_default=False,
        ),
    ]