# Generated by Django 3.0 on 2020-02-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
