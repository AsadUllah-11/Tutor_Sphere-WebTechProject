# Generated by Django 5.0.6 on 2024-07-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_market', '0011_alter_subject_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='iban',
            field=models.CharField(blank=True, max_length=34, null=True),
        ),
    ]