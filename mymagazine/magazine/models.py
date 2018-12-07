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


class Fashion(models.Model):
    article_headline = models.CharField(max_length=100)
    article_dicription = models.CharField(max_length=500)
    article_image = models.FileField()

class Technology(models.Model):
    article_headline = models.CharField(max_length=100)
    article_dicription = models.CharField(max_length=500)
    article_image = models.FileField()

class Health(models.Model):
    article_headline = models.CharField(max_length=100)
    article_dicription = models.CharField(max_length=500)
    article_image = models.FileField()


