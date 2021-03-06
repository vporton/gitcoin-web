# Generated by Django 2.2.3 on 2019-09-22 14:57

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0052_auto_20190919_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, default='')),
                ('game_schema', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('game_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('success', models.BooleanField(default=False)),
                ('coupon_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coupon', to='quests.Quest')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_attempts', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
