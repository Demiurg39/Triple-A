# from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import os

def poster_upload_path(instance, filename):
    return os.path.join("Games_images", instance.slug, filename)

class SystemRequirements(models.Model):
    OS_version = models.CharField("Версия ОП", max_length=100)
    CPU = models.CharField("Пpoцeccop", max_length=100)
    RAM = models.PositiveIntegerField("0ЗУ")
    GPU = models.CharField("Bидеoкaрта", max_length=100)
    Storage = models.PositiveIntegerField("Память")
    Language_dub = models.CharField("Язык озвучивания", max_length=100)
    Language_sub = models.CharField("Язык текста", max_length=100)

    class Meta:
        verbose_name = "SystemRequirement"
        verbose_name_plural = "SystemRequirements"

class Games(models.Model):
    title = models.CharField("Game title", max_length=50)
    slug = models.SlugField("Slug field", max_length=50)
    rating = models.FloatField("Game rating")
    description = models.TextField("Game description")
    poster = models.ImageField("Game poster", upload_to=poster_upload_path)
    rent = models.FloatField("Rent cost per weak")
    buy = models.FloatField("Cost")
    systemreq = models.ForeignKey(
        SystemRequirements,
        on_delete=models.CASCADE,
        related_name="game_requirements",
    )
    added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        ordering = ["-added"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main_app:game_detail', args=[str(self.slug)])

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.game.title} - {self.created_at}"
