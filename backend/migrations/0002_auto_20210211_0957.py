# Generated by Django 3.0.5 on 2021-02-11 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meme',
            old_name='author',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='meme',
            name='url',
            field=models.URLField(max_length=300),
        ),
    ]
