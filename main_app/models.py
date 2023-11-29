from django.db import models
from django.urls import reverse
from django.utils import timezone


def poster_upload_path(instance, filename):
    return f"Games_images/{instance.slug}/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]


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
    name = models.CharField("Game title", max_length=250)
    slug = models.SlugField("Slug field", max_length=250)
    rating = models.FloatField("Game rating")
    description = models.TextField("Game description", blank=True)
    image = models.ImageField(
        "Game poster",
        upload_to=poster_upload_path,
        blank=True,
    )
    rent = models.FloatField("Rent price per weak")
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    systemreq = models.ForeignKey(
        SystemRequirements,
        on_delete=models.CASCADE,
        related_name="game_req",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="category",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "main_app:game_detail",
            args=[self.id, self.slug],
        )
