# Generated by Django 3.0.4 on 2020-04-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_helper', '0003_auto_20200415_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classplan',
            name='uid',
            field=models.CharField(max_length=8),
        ),
    ]