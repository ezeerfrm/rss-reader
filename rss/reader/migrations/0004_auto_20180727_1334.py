# Generated by Django 2.0.7 on 2018-07-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0003_auto_20180726_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
