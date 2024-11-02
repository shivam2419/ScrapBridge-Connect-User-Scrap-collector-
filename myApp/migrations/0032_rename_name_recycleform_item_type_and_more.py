# Generated by Django 5.0.4 on 2024-10-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0031_payments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recycleform',
            old_name='name',
            new_name='item_type',
        ),
        migrations.RemoveField(
            model_name='recycleform',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='recycleform',
            name='facility',
        ),
        migrations.RemoveField(
            model_name='recycleform',
            name='model',
        ),
        migrations.RemoveField(
            model_name='recycleform',
            name='organisation_name',
        ),
        migrations.RemoveField(
            model_name='recycleform',
            name='price',
        ),
        migrations.RemoveField(
            model_name='recycleform',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='recycleform',
            name='date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recycleform',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recycleform',
            name='organisation_id',
            field=models.CharField(default=1, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recycleform',
            name='status',
            field=models.CharField(default=False, max_length=10, null=True),
        ),
    ]