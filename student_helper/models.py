from django.db import models


# Create your models here.
class Users(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    password = models.CharField(max_length=20)


class ClassPlan(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    cid = models.CharField(max_length=20)
    cname = models.CharField(max_length=70)
    pid = models.CharField(max_length=4, null=True, blank=True)
    pname = models.CharField(max_length=30, null=True, blank=True)
    week = models.CharField(max_length=54)
    position = models.CharField(max_length=23)

    class Meta:
        unique_together = ("id", "cid", "week", "position")


class poem(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    sentence = models.CharField(max_length=50)
    origin = models.CharField(max_length=40)
