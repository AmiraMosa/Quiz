# Generated by Django 2.2 on 2019-04-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizModule', '0011_auto_20190409_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]