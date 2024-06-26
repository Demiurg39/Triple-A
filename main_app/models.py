from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone

def poster_upload_path(instance, filename):
    return f"Games_images/{instance.slug}/{filename}"


def validate_float_range(value):
    if not 0 < value < 100:
        raise ValidationError("Value must be between 0 and 100.")


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return self.name


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
    rating = models.FloatField("Game rating", validators=[validate_float_range])
    description = models.TextField("Game description", blank=True)
    image = models.ImageField(
        "Game poster",
        upload_to=poster_upload_path,
        blank=True,
    )
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    systemreq = models.ForeignKey(
        SystemRequirements,
        on_delete=models.CASCADE,
        related_name="game_req",
    )
    categories = models.ManyToManyField(
        Category,
        related_name="categories",
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


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_at"]
        indexes = [
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.game.name} - {self.created_at}"
