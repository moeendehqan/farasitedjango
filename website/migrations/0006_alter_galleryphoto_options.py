# Generated by Django 5.0.4 on 2024-04-22 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_logo_information_logo1_information_logo2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryphoto',
            options={'ordering': ['CreateAt']},
        ),
    ]
