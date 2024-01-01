# Generated by Django 4.2.4 on 2023-12-31 03:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "outfitGenerator",
            "0016_alter_bottomclothing_colour_alter_shoe_colour_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="bottomclothing",
            name="colour",
            field=models.CharField(
                choices=[
                    ("#FF0000", "Red"),
                    ("#FF5349", "Red-Orange"),
                    ("#FFA500", "Orange"),
                    ("#F5BD1F", "Yellow-Orange"),
                    ("#FFFF00", "Yellow"),
                    ("#9ACD32", "Yellow-Green"),
                    ("#00FF00", "Green"),
                    ("#0D98BA", "Blue-Green"),
                    ("#0000FF", "Blue"),
                    ("#8A2BE2", "Blue-Violet"),
                    ("#7F00FF", "Violet"),
                    ("#922B3E", "Red-Violet"),
                    ("#242526", "Black"),
                    ("#F7F5F0", "White"),
                    ("#964B00", "Brown"),
                ],
                default="#FF0000",
                max_length=17,
            ),
        ),
        migrations.AlterField(
            model_name="shoe",
            name="colour",
            field=models.CharField(
                choices=[
                    ("#FF0000", "Red"),
                    ("#FF5349", "Red-Orange"),
                    ("#FFA500", "Orange"),
                    ("#F5BD1F", "Yellow-Orange"),
                    ("#FFFF00", "Yellow"),
                    ("#9ACD32", "Yellow-Green"),
                    ("#00FF00", "Green"),
                    ("#0D98BA", "Blue-Green"),
                    ("#0000FF", "Blue"),
                    ("#8A2BE2", "Blue-Violet"),
                    ("#7F00FF", "Violet"),
                    ("#922B3E", "Red-Violet"),
                    ("#242526", "Black"),
                    ("#F7F5F0", "White"),
                    ("#964B00", "Brown"),
                ],
                default="#FF0000",
                max_length=17,
            ),
        ),
        migrations.AlterField(
            model_name="topclothing",
            name="colour",
            field=models.CharField(
                choices=[
                    ("#FF0000", "Red"),
                    ("#FF5349", "Red-Orange"),
                    ("#FFA500", "Orange"),
                    ("#F5BD1F", "Yellow-Orange"),
                    ("#FFFF00", "Yellow"),
                    ("#9ACD32", "Yellow-Green"),
                    ("#00FF00", "Green"),
                    ("#0D98BA", "Blue-Green"),
                    ("#0000FF", "Blue"),
                    ("#8A2BE2", "Blue-Violet"),
                    ("#7F00FF", "Violet"),
                    ("#922B3E", "Red-Violet"),
                    ("#242526", "Black"),
                    ("#F7F5F0", "White"),
                    ("#964B00", "Brown"),
                ],
                default="#FF0000",
                max_length=17,
            ),
        ),
        migrations.AddIndex(
            model_name="bottomclothing",
            index=models.Index(fields=["user"], name="outfitGener_user_id_689a28_idx"),
        ),
        migrations.AddIndex(
            model_name="bottomclothing",
            index=models.Index(
                fields=["saturation"], name="outfitGener_saturat_74e932_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="bottomclothing",
            index=models.Index(
                fields=["tint_or_shade"], name="outfitGener_tint_or_eb030f_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="bottomclothing",
            index=models.Index(fields=["colour"], name="outfitGener_colour_57471b_idx"),
        ),
        migrations.AddIndex(
            model_name="shoe",
            index=models.Index(fields=["user"], name="outfitGener_user_id_9452d7_idx"),
        ),
        migrations.AddIndex(
            model_name="shoe",
            index=models.Index(
                fields=["saturation"], name="outfitGener_saturat_f16e8a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="shoe",
            index=models.Index(
                fields=["tint_or_shade"], name="outfitGener_tint_or_1ec3ee_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="shoe",
            index=models.Index(fields=["colour"], name="outfitGener_colour_0e22f7_idx"),
        ),
        migrations.AddIndex(
            model_name="topclothing",
            index=models.Index(fields=["user"], name="outfitGener_user_id_ab53de_idx"),
        ),
        migrations.AddIndex(
            model_name="topclothing",
            index=models.Index(
                fields=["saturation"], name="outfitGener_saturat_dd6721_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="topclothing",
            index=models.Index(
                fields=["tint_or_shade"], name="outfitGener_tint_or_6c3fa5_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="topclothing",
            index=models.Index(fields=["colour"], name="outfitGener_colour_172b90_idx"),
        ),
    ]