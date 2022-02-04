from django.db import models

class Login(models.Model):
    user = models.CharField(max_length=20, default=None)
    password = models.CharField(max_length=20, default=None)
