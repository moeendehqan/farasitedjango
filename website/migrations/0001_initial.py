# Generated by Django 5.0.4 on 2024-04-21 05:17

import django.core.validators
import website.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchsOfCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=255)),
                ('Province', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=255)),
                ('Telephone', models.CharField(max_length=20)),
                ('Code', models.CharField(max_length=5)),
                ('Types', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPartners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Logo', models.ImageField(upload_to='static/images/')),
                ('Link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(blank=True, max_length=200, null=True)),
                ('Phonenumber', models.CharField(blank=True, max_length=12, null=True)),
                ('Subject', models.CharField(max_length=200)),
                ('Message', models.CharField(max_length=1000)),
                ('Domain', models.CharField(max_length=255)),
                ('route', models.CharField(max_length=255)),
                ('CreateAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=64)),
                ('owner', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Domain', models.CharField(max_length=255)),
                ('CreateAt', models.DateTimeField()),
                ('SenderEmail', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=255)),
                ('Picture', models.ImageField(upload_to='static/images/')),
                ('Alt', models.CharField(max_length=255)),
                ('route', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=255)),
                ('Video', models.FileField(upload_to='static/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi']), website.models.validate_file_size])),
                ('Alt', models.CharField(max_length=255)),
                ('route', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=255)),
                ('Title', models.CharField(max_length=255)),
                ('Icone', models.ImageField(upload_to='static/images/')),
                ('Url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HistoryOfCompanies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Date', models.CharField(max_length=12)),
                ('Title', models.CharField(max_length=255)),
                ('Paragraph', models.TextField(blank=True, null=True)),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Video', models.FileField(blank=True, null=True, upload_to='static/images/')),
                ('Domain', models.CharField(max_length=255)),
                ('Icon', models.ImageField(blank=True, null=True, upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Logo', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Logotext', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Domain', models.CharField(blank=True, max_length=255, null=True)),
                ('Name', models.CharField(max_length=255)),
                ('Telephone1', models.CharField(max_length=255)),
                ('Telephone2', models.CharField(max_length=255)),
                ('Fax', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('NationalID', models.CharField(max_length=12)),
                ('AboutUs', models.TextField()),
                ('Theme', models.IntegerField(blank=True, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('telegram', models.CharField(blank=True, max_length=255, null=True)),
                ('tweeter', models.CharField(blank=True, max_length=255, null=True)),
                ('Cataloge', models.CharField(blank=True, max_length=255, null=True)),
                ('Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Keywords', models.CharField(blank=True, max_length=500, null=True)),
                ('Admin', models.CharField(max_length=255)),
                ('Date', models.CharField(max_length=255)),
                ('FieldOfActivity', models.CharField(max_length=255)),
                ('TypeOfCompany', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IntroductionOfCompanies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo', models.ImageField(upload_to='static/images/')),
                ('Name', models.CharField(max_length=255)),
                ('Link', models.CharField(max_length=255)),
                ('Telephone', models.CharField(max_length=12)),
                ('Address', models.CharField(max_length=500)),
                ('ShortAboutUs', models.TextField()),
                ('LongAboutUs', models.TextField()),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('telegram', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('Size', models.IntegerField()),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=255)),
                ('Content', models.TextField()),
                ('KeyWord', models.CharField(max_length=500)),
                ('Grouping', models.CharField(max_length=255)),
                ('Title', models.CharField(max_length=500)),
                ('TypeOfContent', models.CharField(max_length=255)),
                ('ShortDescription', models.CharField(max_length=700)),
                ('route', models.CharField(max_length=255)),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=255)),
                ('Picture', models.ImageField(upload_to='static/images/')),
                ('Paragraph', models.TextField()),
                ('Title', models.CharField(max_length=255)),
                ('route', models.CharField(max_length=255)),
                ('AdditionalImages', models.ImageField(blank=True, null=True, upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Date', models.CharField(max_length=12)),
                ('Title', models.CharField(max_length=255)),
                ('Paragraph', models.TextField(blank=True, null=True)),
                ('File', models.FileField(blank=True, null=True, upload_to='static/pdf/')),
                ('Domain', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=500)),
                ('Answer', models.TextField()),
                ('Domain', models.CharField(max_length=255)),
                ('CreateAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='QuickAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=255)),
                ('Url', models.CharField(max_length=255)),
                ('Picture', models.ImageField(upload_to='static/images/')),
                ('Title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiveEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Domain', models.CharField(max_length=255)),
                ('Receiver', models.CharField(max_length=255)),
                ('Sender', models.CharField(max_length=255)),
                ('Body', models.CharField(max_length=10000)),
                ('Subject', models.CharField(max_length=300)),
                ('CreateAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RelatedLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=255)),
                ('Link', models.CharField(max_length=255)),
                ('Title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Domain', models.CharField(max_length=300)),
                ('CreateAt', models.DateTimeField()),
                ('Recipient', models.CharField(max_length=300)),
                ('Subject', models.CharField(max_length=300)),
                ('Body', models.CharField(max_length=10000)),
                ('SenderEmail', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.ImageField(upload_to='static/images/')),
                ('Title', models.CharField(max_length=300)),
                ('Alt', models.CharField(max_length=300)),
                ('Domain', models.CharField(max_length=300)),
                ('CreateAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=300)),
                ('Title', models.CharField(max_length=300)),
                ('Number', models.CharField(max_length=300)),
                ('Icon', models.ImageField(blank=True, null=True, upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField()),
                ('Domain', models.CharField(max_length=300)),
                ('Title', models.CharField(max_length=300)),
            ],
        ),
    ]
