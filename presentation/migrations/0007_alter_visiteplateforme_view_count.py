# Generated by Django 5.1.2 on 2024-11-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0006_visiteplateforme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visiteplateforme',
            name='view_count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
