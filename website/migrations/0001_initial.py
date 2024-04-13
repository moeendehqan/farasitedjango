# Generated by Django 4.1.13 on 2024-04-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Logo', models.CharField(max_length=255)),
                ('Logotext', models.CharField(max_length=255)),
                ('Domain', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Telephone', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('NationalID', models.CharField(max_length=12)),
                ('AboutUs', models.CharField(max_length=700)),
                ('Theme', models.IntegerField()),
                ('instagram', models.IntegerField()),
                ('telegram', models.IntegerField()),
                ('tweeter', models.IntegerField()),
                ('Cataloge', models.CharField(max_length=255)),
                ('Description', models.CharField(max_length=500)),
                ('Keywords', models.CharField(max_length=500)),
                ('Admin', models.CharField(max_length=255)),
                ('Date', models.CharField(max_length=255)),
                ('FieldOfActivity', models.CharField(max_length=255)),
            ],
        ),
    ]