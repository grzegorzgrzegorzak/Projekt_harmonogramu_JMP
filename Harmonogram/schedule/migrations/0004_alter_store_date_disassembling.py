# Generated by Django 4.1.3 on 2022-12-01 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_alter_subcontractor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='date_disassembling',
            field=models.DateTimeField(null=True),
        ),
    ]
