# Generated by Django 2.2 on 2019-04-09 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizModule', '0006_auto_20190409_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='Score_Point',
        ),
    ]
