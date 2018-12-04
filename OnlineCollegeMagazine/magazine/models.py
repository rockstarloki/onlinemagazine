from django.db import models



class UserRegistration(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=50)


class ModeratorRegistration(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=50)
