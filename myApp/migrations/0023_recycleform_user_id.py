# Generated by Django 4.2.6 on 2024-05-24 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0022_alter_owner_organisation_id_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='recycleform',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]