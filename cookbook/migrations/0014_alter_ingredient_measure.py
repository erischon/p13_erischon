# Generated by Django 3.2.3 on 2021-06-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0013_alter_ingredient_measure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='measure',
            field=models.CharField(max_length=200),
        ),
    ]
