# Generated by Django 3.0.5 on 2022-07-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0008_auto_20220717_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoremodel',
            name='time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]