# Generated by Django 4.0.6 on 2022-10-23 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_alter_response_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='status',
            new_name='confirmed',
        ),
    ]
