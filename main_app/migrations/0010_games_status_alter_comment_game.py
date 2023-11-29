# Generated by Django 4.2.7 on 2023-11-28 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0009_alter_comment_options_comment_active_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="games",
            name="status",
            field=models.CharField(
                choices=[("DF", "Draft"), ("PB", "Published")],
                default="DF",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="game",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="main_app.games",
            ),
        ),
    ]
