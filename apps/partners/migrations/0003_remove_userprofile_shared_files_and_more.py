# Generated by Django 4.2.1 on 2023-05-10 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_userfile_userprofile_userfile_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='shared_files',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserFile',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
