# Generated by Django 2.1.1 on 2021-10-24 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thehunt', '0009_auto_20210909_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='questions',
            name='modelanswer',
        ),
        migrations.RemoveField(
            model_name='users',
            name='fullname2',
        ),
        migrations.AddField(
            model_name='globalvariables',
            name='test_dur',
            field=models.DurationField(default='1:00:00'),
        ),
        migrations.AddField(
            model_name='answers',
            name='lvl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thehunt.Questions'),
        ),
        migrations.AddField(
            model_name='answers',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]