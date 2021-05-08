# Generated by Django 3.2 on 2021-05-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0008_auto_20210429_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_username', models.CharField(max_length=37)),
                ('github_username', models.CharField(blank=True, max_length=39, null=True)),
                ('twitter_username', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
