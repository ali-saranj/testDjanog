# Generated by Django 4.2.6 on 2023-10-06 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_post_title_alter_post_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
    ]
