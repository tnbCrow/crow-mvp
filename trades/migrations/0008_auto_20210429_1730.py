# Generated by Django 3.2 on 2021-04-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0007_statistic_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backupstatistic',
            old_name='rate',
            new_name='weighted_rate',
        ),
        migrations.RenameField(
            model_name='statistic',
            old_name='rate',
            new_name='weighted_rate',
        ),
        migrations.AddField(
            model_name='backupstatistic',
            name='last_rate',
            field=models.IntegerField(default=289),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistic',
            name='last_rate',
            field=models.IntegerField(default=289),
            preserve_default=False,
        ),
    ]
