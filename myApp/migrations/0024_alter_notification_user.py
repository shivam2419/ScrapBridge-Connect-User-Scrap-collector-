# Generated by Django 4.2.6 on 2024-05-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0023_recycleform_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.IntegerField(),
        ),
    ]