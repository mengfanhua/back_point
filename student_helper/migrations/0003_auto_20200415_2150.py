# Generated by Django 3.0.4 on 2020-04-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_helper', '0002_auto_20200330_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='classplan',
            name='semester',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='classplan',
            unique_together={('uid', 'semester', 'cid', 'week', 'position')},
        ),
    ]