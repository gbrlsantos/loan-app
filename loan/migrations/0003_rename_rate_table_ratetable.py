# Generated by Django 3.2.14 on 2022-07-05 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_auto_20220705_2007'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rate_Table',
            new_name='RateTable',
        ),
    ]
