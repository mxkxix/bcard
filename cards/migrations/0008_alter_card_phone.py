# Generated by Django 4.2.8 on 2024-01-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_card_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='phone',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]