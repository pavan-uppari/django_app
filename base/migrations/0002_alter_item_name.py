# Generated by Django 4.2.16 on 2024-10-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
