# Generated by Django 4.2.6 on 2024-05-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0027_recycleform_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recycleform',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='recycleform',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]