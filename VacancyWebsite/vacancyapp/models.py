from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email


class VacancyList(models.Model):
    site = models.CharField(max_length=30)
    url = models.URLField()

    def __str__(self):
        return self.site


class ScrappedData(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ScrappedVacancy(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    due_date = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ScrappedTender(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    posted_date = models.CharField(max_length=20, null=True, blank=True)
    close_date = models.CharField(max_length=20, null=True, blank=True)
    scrapped_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ScrappedAdvert(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    posted_date = models.CharField(max_length=20, null=True, blank=True)
    scrapped_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ScrappedNew(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    site = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_link = models.URLField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    posted_date = models.CharField(max_length=20, null=True, blank=True)
    scrapped_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
