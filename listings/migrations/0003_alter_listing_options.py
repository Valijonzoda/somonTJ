# Generated by Django 5.0.6 on 2024-05-24 19:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0002_listing_delete_listings"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="listing",
            options={"verbose_name_plural": "Listing"},
        ),
    ]
