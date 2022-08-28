from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Experiance(models.Model):
    position = models.TextField()
    company_name = models.TextField()
    joining_date = models.TextField()
    leaving_date = models.TextField()
    desc = models.TextField()
    work = JSONField()


class Projects(models.Model):
    title = models.TextField()
    upload = models.FileField(upload_to='media')
    date = models.TextField()
    desc = models.TextField()
    status = models.TextField()


class Intern(models.Model):
    title = models.TextField()
    comny = models.TextField()
    date = models.TextField()
    desc = models.TextField()


class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    subject = models.TextField()
    text = models.TextField()
