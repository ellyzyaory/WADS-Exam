# Generated by Django 4.0.5 on 2022-06-28 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_menu_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='user_id',
        ),
    ]