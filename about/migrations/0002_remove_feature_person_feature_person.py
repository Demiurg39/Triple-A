# Generated by Django 4.2.7 on 2023-12-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feature",
            name="person",
        ),
        migrations.AddField(
            model_name="feature",
            name="person",
            field=models.ManyToManyField(related_name="person", to="about.person"),
        ),
    ]
