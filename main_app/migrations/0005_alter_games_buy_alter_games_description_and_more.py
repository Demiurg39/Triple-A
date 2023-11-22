# Generated by Django 4.2.7 on 2023-11-22 12:12

from django.db import migrations, models
import django.db.models.deletion
import main_app.models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0004_alter_games_options_games_added"),
    ]

    operations = [
        migrations.AlterField(
            model_name="games",
            name="buy",
            field=models.FloatField(verbose_name="Cost"),
        ),
        migrations.AlterField(
            model_name="games",
            name="description",
            field=models.TextField(verbose_name="Game description"),
        ),
        migrations.AlterField(
            model_name="games",
            name="poster",
            field=models.ImageField(upload_to="games", verbose_name="Game poster"),
        ),
        migrations.AlterField(
            model_name="games",
            name="rating",
            field=models.FloatField(
                validators=[main_app.models.validate_rate], verbose_name="Game rating"
            ),
        ),
        migrations.AlterField(
            model_name="games",
            name="rent",
            field=models.FloatField(verbose_name="Rent cost for weak"),
        ),
        migrations.AlterField(
            model_name="games",
            name="slug",
            field=models.SlugField(verbose_name="Slug field"),
        ),
        migrations.AlterField(
            model_name="games",
            name="systemreq",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="game_req",
                to="main_app.systemrequirements",
            ),
        ),
        migrations.AlterField(
            model_name="games",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Game title"),
        ),
    ]
