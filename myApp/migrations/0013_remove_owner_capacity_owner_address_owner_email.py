# Generated by Django 4.2.6 on 2024-05-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='capacity',
        ),
        migrations.AddField(
            model_name='owner',
            name='address',
            field=models.CharField(default='', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='email',
            field=models.EmailField(default='', max_length=254, null=True),
        ),
    ]