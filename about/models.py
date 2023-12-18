from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='people_images/', null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    person = models.ManyToManyField(Person, related_name='person')
    company = models.ManyToManyField(Company, related_name='company')

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def __str__(self):
        return self.title
