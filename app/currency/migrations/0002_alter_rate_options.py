# Generated by Django 4.1.7 on 2023-04-09 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rate',
            options={'ordering': ('-created',)},
        ),
    ]
