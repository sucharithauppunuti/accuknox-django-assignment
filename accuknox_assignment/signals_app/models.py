from django.db import models


class DemoModel(models.Model):
    name = models.CharField(max_length=100)


class SignalLog(models.Model):
    message = models.CharField(max_length=255)