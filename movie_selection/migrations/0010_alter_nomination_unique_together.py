# Generated by Django 4.1 on 2022-08-12 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movie_selection", "0009_user_username"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="nomination",
            unique_together={("room", "title")},
        ),
    ]
