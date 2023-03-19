# Generated by Django 4.1.6 on 2023-03-18 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0005_alter_rate_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=128)),
                ('request_method', models.CharField(max_length=32)),
                ('time', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=256),
        ),
    ]
