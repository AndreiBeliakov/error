# Generated by Django 4.1.2 on 2022-10-17 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newssite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='price',
        ),
        migrations.AlterField(
            model_name='new',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]