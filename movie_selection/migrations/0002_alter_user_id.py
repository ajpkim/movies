# Generated by Django 4.1 on 2022-08-10 16:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("movie_selection", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
