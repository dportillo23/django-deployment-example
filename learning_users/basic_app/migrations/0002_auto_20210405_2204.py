# Generated by Django 3.1.7 on 2021-04-05 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='picture',
            new_name='profile_pic',
        ),
    ]
