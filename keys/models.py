from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from main_app.models import Games


class Keys(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='game')
    code = models.CharField(max_length=50, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    period = models.IntegerField(default=7)
    discount = models.FloatField(default=0.05)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, default='active')

    def calculate_rent_price(self):
        return round(self.discount * float(self.game.price) * self.period, 2)

    def end_date(self):
        return self.start_date + timezone.timedelta(days=self.period)

    @property
    def is_active(self):
        return timezone.now() <= self.end_date()

    def is_valid_code(self, entered_code):
        return self.code == entered_code and self.status == 'sent'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Key"
        verbose_name_plural = "Keys"
