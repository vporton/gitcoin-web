# Generated by Django 2.2.4 on 2020-05-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0025_questpointaward_metadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='questattempt',
            name='last_question',
            field=models.IntegerField(default=-1),
        ),
    ]