# Generated by Django 4.2.7 on 2023-11-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0008_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["created_at"]},
        ),
        migrations.AddField(
            model_name="comment",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddIndex(
            model_name="comment",
            index=models.Index(
                fields=["created_at"], name="main_app_co_created_69df10_idx"
            ),
        ),
    ]
