# Generated by Django 4.2.7 on 2023-11-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemrequirements',
            name='CPU',
            field=models.CharField(max_length=100, verbose_name='Пpoцeccop'),
        ),
        migrations.AlterField(
            model_name='systemrequirements',
            name='Language_dub',
            field=models.CharField(max_length=100, verbose_name='Язык озвучивания'),
        ),
        migrations.AlterField(
            model_name='systemrequirements',
            name='Language_sub',
            field=models.CharField(max_length=100, verbose_name='Язык текста'),
        ),
    ]
