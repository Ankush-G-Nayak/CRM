# Generated by Django 4.2.16 on 2024-11-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='PhNo',
            field=models.CharField(max_length=10),
        ),
    ]