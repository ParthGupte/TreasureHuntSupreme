# Generated by Django 2.1.1 on 2021-10-24 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thehunt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='ans',
            field=models.TextField(default=''),
        ),
    ]
