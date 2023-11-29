# Generated by Django 4.2.7 on 2023-11-28 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0010_games_status_alter_comment_game"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="games",
            name="status",
        ),
        migrations.AlterField(
            model_name="comment",
            name="game",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main_app.games"
            ),
        ),
    ]
