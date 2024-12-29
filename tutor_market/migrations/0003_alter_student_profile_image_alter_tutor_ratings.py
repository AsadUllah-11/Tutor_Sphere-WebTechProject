# Generated by Django 5.0.6 on 2024-07-03 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_market', '0002_tutor_catch_phrase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='student_images'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='ratings',
            field=models.ManyToManyField(blank=True, related_name='tutors', to='tutor_market.rating'),
        ),
    ]
