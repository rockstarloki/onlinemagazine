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


class ModFashion(models.Model):
    article_type = models.CharField(max_length=50)
    article_headline = models.CharField(max_length=100)
    article_dicription = models.CharField(max_length=500)
    article_image = models.FileField()
    user_email = models.CharField(max_length=100)

class ModTechnology(models.Model):
    article_type = models.CharField(max_length=50)
    article_headline = models.CharField(max_length=100)
    article_dicription = models.CharField(max_length=500)
    article_image = models.FileField()
    user_email = models.CharField(max_length=100)

class ModHealth(models.Model):
    article_type = models.CharField(max_length=50)
    article_headline = models.CharField(max_length=100)
    article_dicription = models.CharField(max_length=500)
    article_image = models.FileField()
    user_email = models.CharField(max_length=100)


class HomeFashion(models.Model):
    article_headline = models.CharField(max_length=100)
    article_dicription = models.CharField(max_length=500)
    article_image = models.FileField()

class HomeTechnology(models.Model):
    article_headline = models.CharField(max_length=100)
    article_dicription = models.CharField(max_length=500)
    article_image = models.FileField()

class HomeHealth(models.Model):
    article_headline = models.CharField(max_length=100)
    article_dicription = models.CharField(max_length=500)
    article_image = models.FileField()
