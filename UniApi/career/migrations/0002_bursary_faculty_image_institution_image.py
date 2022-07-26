# Generated by Django 4.0.3 on 2022-07-21 13:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bursary',
            fields=[
                ('bursary_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('bursary_name', models.CharField(max_length=100)),
                ('bursary_logo', models.ImageField(blank=True, default='default.png', null=True, upload_to='bursaries/')),
                ('bursary_description', models.TextField(blank=True, default='Bursary description', null=True)),
                ('bursary_field_study_1', models.TextField(blank=True, null=True)),
                ('bursary_field_study_2', models.TextField(blank=True, null=True)),
                ('bursary_field_study_3', models.TextField(blank=True, null=True)),
                ('bursary_requirements', models.TextField(blank=True, null=True)),
                ('bursary_link', models.CharField(max_length=250)),
                ('bursary_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['bursary_added'],
            },
        ),
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='logo/faculties'),
        ),
        migrations.AddField(
            model_name='institution',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='logo/institutions'),
        ),
    ]
