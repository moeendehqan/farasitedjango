# Generated by Django 5.0.4 on 2024-04-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Grouping',
            field=models.CharField(choices=[], default='مقالات', max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='TypeOfContent',
            field=models.CharField(choices=[], default='مقالات', max_length=255),
        ),
    ]
