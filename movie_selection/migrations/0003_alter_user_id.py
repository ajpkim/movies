# Generated by Django 4.1 on 2022-08-10 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("movie_selection", "0002_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]