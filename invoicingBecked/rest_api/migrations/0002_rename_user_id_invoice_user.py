# Generated by Django 4.1.9 on 2023-07-24 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='user_id',
            new_name='user',
        ),
    ]
