# Generated by Django 4.1.2 on 2022-10-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(default='Z6D4T-rI', editable=False, max_length=8),
        ),
    ]
