# Generated by Django 4.2.4 on 2023-09-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "outfitGenerator",
            "0007_alter_bottomclothing_colour_alter_shoe_colour_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="bottomclothing",
            name="colour",
            field=models.CharField(
                choices=[
                    ("#FF0000", "Red"),
                    ("#FFA500", "Orange"),
                    ("#FFFF00", "Yellow"),
                    ("#9ACD32", "Yellow-Green"),
                    ("#00FF00", "Green"),
                    ("#0D98BA", "Blue-Green"),
                    ("#0000FF", "Blue"),
                    ("#8a2be2", "Blue-Violet"),
                    ("#7F00FF", "Violet"),
                    ("#e0b0ff", "Mauve"),
                    ("#C77398", "Mauve-Pink"),
                    ("#FFC0CB", "Pink"),
                    ("#242526", "Black"),
                    ("#FFFFFF", "white"),
                    ("#808080", "Grey"),
                ],
                default="#FF0000",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="shoe",
            name="colour",
            field=models.CharField(
                choices=[
                    ("#FF0000", "Red"),
                    ("#FFA500", "Orange"),
                    ("#FFFF00", "Yellow"),
                    ("#9ACD32", "Yellow-Green"),
                    ("#00FF00", "Green"),
                    ("#0D98BA", "Blue-Green"),
                    ("#0000FF", "Blue"),
                    ("#8a2be2", "Blue-Violet"),
                    ("#7F00FF", "Violet"),
                    ("#e0b0ff", "Mauve"),
                    ("#C77398", "Mauve-Pink"),
                    ("#FFC0CB", "Pink"),
                    ("#242526", "Black"),
                    ("#FFFFFF", "white"),
                    ("#808080", "Grey"),
                ],
                default="#FF0000",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="topclothing",
            name="colour",
            field=models.CharField(
                choices=[
                    ("#FF0000", "Red"),
                    ("#FFA500", "Orange"),
                    ("#FFFF00", "Yellow"),
                    ("#9ACD32", "Yellow-Green"),
                    ("#00FF00", "Green"),
                    ("#0D98BA", "Blue-Green"),
                    ("#0000FF", "Blue"),
                    ("#8a2be2", "Blue-Violet"),
                    ("#7F00FF", "Violet"),
                    ("#e0b0ff", "Mauve"),
                    ("#C77398", "Mauve-Pink"),
                    ("#FFC0CB", "Pink"),
                    ("#242526", "Black"),
                    ("#FFFFFF", "white"),
                    ("#808080", "Grey"),
                ],
                default="#FF0000",
                max_length=15,
            ),
        ),
    ]
