# Generated by Django 4.0.1 on 2022-07-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tricks', '0007_alter_usertrick_rank_alter_usertrick_trick_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='ready_to_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='yt_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
