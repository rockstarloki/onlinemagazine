# Generated by Django 2.1.2 on 2018-12-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0005_auto_20181208_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='modfashion',
            name='article_type',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modhealth',
            name='article_type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modtechnology',
            name='article_type',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
