# Generated by Django 5.1 on 2024-09-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("public", "0004_remove_armes_user_remove_inventaires_weapons_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="skins",
            name="image",
            field=models.ImageField(null=True, upload_to="skins/"),
        ),
    ]
