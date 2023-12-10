from django.db import models

class FAQ(models.Model):
    title = models.CharField(max_length=100)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
