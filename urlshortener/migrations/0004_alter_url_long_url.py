# Generated by Django 4.1.2 on 2022-10-15 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0003_alter_url_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='long_url',
            field=models.URLField(max_length=255),
        ),
    ]