# Generated by Django 4.1.3 on 2023-01-04 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='store_street_number',
            field=models.CharField(max_length=30),
        ),
    ]