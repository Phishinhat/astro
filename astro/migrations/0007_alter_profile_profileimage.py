# Generated by Django 5.0.1 on 2024-05-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astro', '0006_alter_profile_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileImage',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
