# Generated by Django 2.0.7 on 2018-07-24 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='nom',
            field=models.CharField(default='', max_length=1000),
        ),
    ]