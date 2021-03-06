# Generated by Django 2.0.7 on 2018-07-24 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('pubDate', models.DateField()),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('starred', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Rss_a_suivre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=1000)),
                ('lien', models.URLField(max_length=1000)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.Categorie')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='origine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.Rss_a_suivre'),
        ),
    ]
