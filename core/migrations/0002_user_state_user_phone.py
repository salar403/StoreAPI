# Generated by Django 4.0.3 on 2022-05-16 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='State',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.DecimalField(decimal_places=0, max_digits=9, null=True),
        ),
    ]
