# Generated by Django 3.0.4 on 2020-03-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='poem',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('sentence', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ClassPlan',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('cid', models.CharField(max_length=20)),
                ('cname', models.CharField(max_length=70)),
                ('pid', models.CharField(blank=True, max_length=4, null=True)),
                ('pname', models.CharField(blank=True, max_length=30, null=True)),
                ('week', models.CharField(max_length=54)),
                ('position', models.CharField(max_length=23)),
            ],
            options={
                'unique_together': {('id', 'cid', 'week', 'position')},
            },
        ),
    ]
