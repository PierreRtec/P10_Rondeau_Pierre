from django.db import models


class Users(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
