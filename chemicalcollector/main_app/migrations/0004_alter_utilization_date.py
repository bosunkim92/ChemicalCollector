# Generated by Django 3.2.5 on 2021-07-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_utilization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilization',
            name='date',
            field=models.DateField(verbose_name='used date'),
        ),
    ]
