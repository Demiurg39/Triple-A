# Generated by Django 4.2.7 on 2023-12-05 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main_app", "0004_remove_games_category_games_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="games",
            name="categories",
            field=models.ManyToManyField(
                related_name="categories", to="main_app.category"
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("active", models.BooleanField(default=True)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main_app.games"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
                "indexes": [
                    models.Index(
                        fields=["created_at"], name="main_app_co_created_69df10_idx"
                    )
                ],
            },
        ),
    ]