# Generated by Django 4.0 on 2021-12-07 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_id',
            field=models.CharField(default='', max_length=10),
        ),
    ]
