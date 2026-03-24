from django.db import models

class Foydalanuvchi(models.Model):
    username = models.CharField
    userid = models.BigIntegerField(unique=True)

