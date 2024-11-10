# Generated by Django 5.1.2 on 2024-11-10 18:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0005_remove_entreprise_logo_entreprise_nb_experience_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitePlateforme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('device_type', models.CharField(max_length=50)),
                ('view_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
