# Generated by Django 5.1.3 on 2024-12-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='otp',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
