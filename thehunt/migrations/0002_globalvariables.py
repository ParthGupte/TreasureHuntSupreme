# Generated by Django 2.1.1 on 2021-09-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thehunt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalVariables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_start', models.DateTimeField()),
                ('test_end', models.DateTimeField()),
            ],
        ),
    ]
