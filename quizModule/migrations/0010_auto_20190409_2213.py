# Generated by Django 2.2 on 2019-04-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizModule', '0009_auto_20190409_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz_id',
        ),
        migrations.AddField(
            model_name='question',
            name='quiz_id',
            field=models.ManyToManyField(null=True, to='quizModule.Quiz'),
        ),
    ]
