# Generated by Django 3.2.13 on 2022-06-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='court',
            field=models.CharField(default='default', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
