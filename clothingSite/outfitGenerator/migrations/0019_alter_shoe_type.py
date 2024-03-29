# Generated by Django 4.2.4 on 2024-01-01 05:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("outfitGenerator", "0018_bottomclothing_formality_shoe_formality_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shoe",
            name="type",
            field=models.CharField(
                choices=[
                    ("Sport Sneakers", "Sport Sneakers"),
                    ("Dress Shoes", "Dress Shoes"),
                ],
                default="Sport Sneakers",
                max_length=15,
            ),
        ),
    ]
