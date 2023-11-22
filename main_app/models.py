from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone


def validate_rate(value):
    if not (1.0 <= value <= 10.0):
        raise ValidationError("Rate must be between 1.0 and 10.0")


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
    rating = models.FloatField("Game rating", validators=[validate_rate])
    description = models.TextField("Game description")
    poster = models.ImageField(
        "Game poster",
        upload_to=f"Games_images/{title}",
    )
    rent = models.FloatField("Rent cost for weak")
    buy = models.FloatField("Cost")
    systemreq = models.ForeignKey(
        SystemRequirements,
        on_delete=models.CASCADE,
        related_name="game_req",
    )
    added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        ordering = ["-added"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "main_app:game_detail",
            args=[self.slug],
        )
