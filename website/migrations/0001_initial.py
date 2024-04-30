# Generated by Django 5.0.4 on 2024-04-30 08:24

import colorfield.fields
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import website.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=64, unique=True)),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'دامنه',
                'verbose_name_plural': 'دامنه ها',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('recipients', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('sender', models.CharField(choices=[('info@isatispooya.com', 'info'), ('admin@isatispooya.com', 'admin'), ('fidip@isatispooya.com', 'fidip')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContentTabs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Title', models.TextField()),
                ('Description', models.TextField(blank=True, null=True)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content Tabs',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(blank=True, max_length=200, null=True)),
                ('Phonenumber', models.CharField(blank=True, max_length=12, null=True)),
                ('Subject', models.CharField(max_length=200)),
                ('Message', models.CharField(max_length=1000)),
                ('route', models.CharField(max_length=255)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us Form',
            },
        ),
        migrations.CreateModel(
            name='BusinessPartners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Name', models.CharField(max_length=255)),
                ('Logo', models.ImageField(upload_to='static/images/')),
                ('Link', models.CharField(max_length=255)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain')),
            ],
            options={
                'verbose_name': 'BusinessPartner',
                'verbose_name_plural': 'BusinessPartners',
            },
        ),
        migrations.CreateModel(
            name='BranchsOfCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Province', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=255)),
                ('MapLink', models.CharField(max_length=255)),
                ('Telephone', models.CharField(max_length=20)),
                ('Code', models.CharField(max_length=5)),
                ('Types', models.CharField(max_length=100)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branchs',
            },
        ),
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Picture', models.ImageField(upload_to='static/images/')),
                ('Alt', models.CharField(max_length=255)),
                ('route', models.CharField(max_length=255)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Gallery Photo',
                'ordering': ['-CreateAt'],
            },
        ),
        migrations.CreateModel(
            name='GalleryVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Video', models.FileField(upload_to='static/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi']), website.models.validate_file_size])),
                ('ShortVideo', models.FileField(upload_to='static/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi']), website.models.validate_file_size])),
                ('Alt', models.CharField(max_length=255)),
                ('route', models.CharField(max_length=255)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Gallery Video',
            },
        ),
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Title', models.CharField(max_length=255)),
                ('Icone', models.ImageField(upload_to='static/images/')),
                ('Url', models.CharField(max_length=255)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Grouping',
            },
        ),
        migrations.CreateModel(
            name='HistoryOfCompanies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Date', models.CharField(max_length=12)),
                ('Title', models.CharField(max_length=255)),
                ('Paragraph', models.TextField(blank=True, null=True)),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Video', models.FileField(blank=True, null=True, upload_to='static/images/')),
                ('Icon', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'History',
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Logo1', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Logo2', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Logotext', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Name', models.CharField(max_length=255)),
                ('Telephone1', models.CharField(max_length=255)),
                ('Telephone2', models.CharField(max_length=255)),
                ('Fax', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('NationalID', models.CharField(max_length=12)),
                ('AboutUs', models.TextField()),
                ('Theme', models.IntegerField(blank=True, null=True)),
                ('MapLink', models.CharField(max_length=255)),
                ('Email', models.EmailField(blank=True, max_length=255, null=True)),
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
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Informations',
                'verbose_name_plural': 'Informations',
            },
        ),
        migrations.CreateModel(
            name='IntroductionOfCompanies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Logo', models.ImageField(upload_to='static/images/')),
                ('Name', models.CharField(max_length=255)),
                ('Link', models.CharField(max_length=255)),
                ('Telephone', models.CharField(max_length=12)),
                ('Address', models.CharField(max_length=500)),
                ('ShortAboutUs', models.TextField(max_length=80)),
                ('LongAboutUs', models.TextField(blank=True, null=True)),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('SubName', models.CharField(blank=True, max_length=255, null=True)),
                ('Size', models.IntegerField()),
                ('Background', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('MegaMenu', models.CharField(max_length=255)),
                ('Title', models.CharField(max_length=500)),
                ('Link', models.CharField(max_length=255)),
                ('Icon', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Links',
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Content', models.TextField()),
                ('KeyWord', models.CharField(max_length=500)),
                ('Title', models.CharField(max_length=500)),
                ('ShortDescription', models.CharField(max_length=700)),
                ('route', models.CharField(max_length=255)),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
                ('Grouping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.grouping')),
            ],
            options={
                'verbose_name': 'New',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='positionofmanagers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=300)),
                ('Senior', models.CharField(blank=True, max_length=300, null=True)),
                ('Level', models.IntegerField()),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Position Of Managers',
            },
        ),
        migrations.CreateModel(
            name='ManagersPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=300)),
                ('Name', models.CharField(max_length=300)),
                ('Telephone', models.CharField(max_length=300)),
                ('Email', models.CharField(max_length=300)),
                ('Picture', models.ImageField(upload_to='static/images/')),
                ('Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.positionofmanagers')),
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Managers',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Picture', models.ImageField(upload_to='static/images/')),
                ('Paragraph', models.TextField()),
                ('Title', models.CharField(max_length=255)),
                ('route', models.CharField(max_length=255)),
                ('AdditionalImages', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Date', models.CharField(max_length=12)),
                ('Title', models.CharField(max_length=255)),
                ('Paragraph', models.TextField(blank=True, null=True)),
                ('File', models.FileField(blank=True, null=True, upload_to='static/pdf/')),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Project Progress',
            },
        ),
        migrations.CreateModel(
            name='QaOfContentTabs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Question', models.TextField()),
                ('Answer', models.TextField(blank=True, null=True)),
                ('Image', models.ImageField(upload_to='static/images/')),
                ('Link', models.CharField(max_length=150)),
                ('ContentTabs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.contenttabs')),
            ],
            options={
                'verbose_name': 'QA',
                'verbose_name_plural': 'QA Of Content Tabs',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Question', models.CharField(max_length=500)),
                ('Answer', models.TextField()),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Questions & Answer',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='QuickAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Url', models.CharField(max_length=255)),
                ('Picture', models.ImageField(upload_to='static/images/')),
                ('Title', models.CharField(max_length=500)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Links',
                'verbose_name_plural': 'QuickAccess',
            },
        ),
        migrations.CreateModel(
            name='ReceiveEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receiver', models.CharField(max_length=255)),
                ('Sender', models.CharField(max_length=255)),
                ('Body', models.CharField(max_length=10000)),
                ('Subject', models.CharField(max_length=300)),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Title', models.CharField(max_length=300)),
                ('Link', models.CharField(max_length=255)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Links',
                'verbose_name_plural': 'Related Links',
            },
        ),
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Recipient', models.CharField(max_length=300)),
                ('Subject', models.CharField(max_length=300)),
                ('Body', models.CharField(max_length=10000)),
                ('SenderEmail', models.CharField(max_length=300)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Picture', models.ImageField(upload_to='static/images/')),
                ('Title', models.CharField(max_length=300)),
                ('Alt', models.CharField(max_length=300)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slider',
            },
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Title', models.CharField(max_length=300)),
                ('Number', models.CharField(max_length=300)),
                ('Icon', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Statistics',
                'verbose_name_plural': 'Statistics',
            },
        ),
        migrations.CreateModel(
            name='SubjectSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Title', models.CharField(max_length=300)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subject Subscription',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Subject', models.CharField(max_length=300)),
                ('Telephone', models.CharField(max_length=12)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Sub',
                'verbose_name_plural': 'Subscription',
            },
        ),
        migrations.CreateModel(
            name='TypeOfContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('Title', models.CharField(max_length=300)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.domain', to_field='domain')),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Type Of Content',
            },
        ),
    ]
