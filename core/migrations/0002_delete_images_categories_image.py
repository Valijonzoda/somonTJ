# Generated by Django 5.0.6 on 2024-05-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Images",
        ),
        migrations.AddField(
            model_name="categories",
            name="image",
            field=models.ImageField(
                default="images/categories/default.jpg", upload_to="images/categories/"
            ),
        ),
    ]