# Generated by Django 4.1 on 2022-08-10 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movie_selection", "0007_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
