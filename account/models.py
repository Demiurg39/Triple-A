from django.conf import settings
from django.db import models


def path_to_profile_photo(instance, filename):
    return f"profiles/{instance.user.username}/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=path_to_profile_photo)

    def __str__(self):
        return f"Profile of {self.user.username}"
