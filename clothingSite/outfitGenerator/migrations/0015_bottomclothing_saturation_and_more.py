# Generated by Django 4.2.4 on 2023-09-23 22:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "outfitGenerator",
            "0014_alter_bottomclothing_colour_alter_shoe_colour_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="bottomclothing",
            name="saturation",
            field=models.PositiveIntegerField(
                default=100, validators=[django.core.validators.MaxValueValidator(100)]
            ),
        ),
        migrations.AddField(
            model_name="bottomclothing",
            name="tint_or_shade",
            field=models.PositiveIntegerField(
                default=100, validators=[django.core.validators.MaxValueValidator(200)]
            ),
        ),
        migrations.AddField(
            model_name="shoe",
            name="saturation",
            field=models.PositiveIntegerField(
                default=100, validators=[django.core.validators.MaxValueValidator(100)]
            ),
        ),
        migrations.AddField(
            model_name="shoe",
            name="tint_or_shade",
            field=models.PositiveIntegerField(
                default=100, validators=[django.core.validators.MaxValueValidator(200)]
            ),
        ),
        migrations.AddField(
            model_name="topclothing",
            name="saturation",
            field=models.PositiveIntegerField(
                default=100, validators=[django.core.validators.MaxValueValidator(100)]
            ),
        ),
        migrations.AddField(
            model_name="topclothing",
            name="tint_or_shade",
            field=models.PositiveIntegerField(
                default=100, validators=[django.core.validators.MaxValueValidator(200)]
            ),
        ),
        migrations.AlterField(
            model_name="bottomclothing",
            name="colour",
            field=models.CharField(
                choices=[
                    ("#ffb3b3", "Red #1"),
                    ("#ff9999", "Red #2"),
                    ("#ff8080", "Red #3"),
                    ("#ff6666", "Red #4"),
                    ("#ff4d4d", "Red #5"),
                    ("#ff3333", "Red #6"),
                    ("#ff1a1a", "Red #7"),
                    ("#ff0000", "Red #8"),
                    ("#e60000", "Red #9"),
                    ("#cc0000", "Red #10"),
                    ("#b30000", "Red #11"),
                    ("#990000", "Red #12"),
                    ("#800000", "Red #13"),
                    ("#660000", "Red #14"),
                    ("#4c0000", "Red #15"),
                    ("#ffcbc8", "Red-Orange #1"),
                    ("#ffbab6", "Red-Orange #2"),
                    ("#ffa9a4", "Red-Orange #3"),
                    ("#ff9892", "Red-Orange #4"),
                    ("#ff8780", "Red-Orange #5"),
                    ("#ff756d", "Red-Orange #6"),
                    ("#ff645b", "Red-Orange #7"),
                    ("#ff5349", "Red-Orange #8"),
                    ("#e64b42", "Red-Orange #9"),
                    ("#cc423a", "Red-Orange #10"),
                    ("#b33a33", "Red-Orange #11"),
                    ("#99322c", "Red-Orange #12"),
                    ("#802a25", "Red-Orange #13"),
                    ("#66211d", "Red-Orange #14"),
                    ("#4c1916", "Red-Orange #15"),
                    ("#ffe4b3", "Orange #1"),
                    ("#ffdb99", "Orange #2"),
                    ("#ffd280", "Orange #3"),
                    ("#ffc966", "Orange #4"),
                    ("#ffc04d", "Orange #5"),
                    ("#ffb733", "Orange #6"),
                    ("#ffae1a", "Orange #7"),
                    ("#ffa500", "Orange #8"),
                    ("#e69500", "Orange #9"),
                    ("#cc8400", "Orange #10"),
                    ("#fcebbc", "Yellow-Orange #1"),
                    ("#fbe5a5", "Yellow-Orange #2"),
                    ("#fade8f", "Yellow-Orange #3"),
                    ("#f9d779", "Yellow-Orange #4"),
                    ("#f8d162", "Yellow-Orange #5"),
                    ("#f7ca4c", "Yellow-Orange #6"),
                    ("#f6c435", "Yellow-Orange #7"),
                    ("#f5bd1f", "Yellow-Orange #8"),
                    ("#ddaa1c", "Yellow-Orange #9"),
                    ("#c49719", "Yellow-Orange #10"),
                    ("#ac8416", "Yellow-Orange #11"),
                    ("#937113", "Yellow-Orange #12"),
                    ("#7b5f10", "Yellow-Orange #13"),
                    ("#624c0c", "Yellow-Orange #14"),
                    ("#493909", "Yellow-Orange #15"),
                    ("#ffffb3", "Yellow #1"),
                    ("#ffff99", "Yellow #2"),
                    ("#ffff80", "Yellow #3"),
                    ("#ffff66", "Yellow #4"),
                    ("#ffff4d", "Yellow #5"),
                    ("#ffff33", "Yellow #6"),
                    ("#ffff1a", "Yellow #7"),
                    ("#ffff00", "Yellow #8"),
                    ("#e6e600", "Yellow #9"),
                    ("#cccc00", "Yellow #10"),
                    ("#b3b300", "Yellow #11"),
                    ("#999900", "Yellow #12"),
                    ("#808000", "Yellow #13"),
                    ("#666600", "Yellow #14"),
                    ("#4c4c00", "Yellow #15"),
                    ("#e1f0c2", "Yellow-Green #1"),
                    ("#d7ebad", "Yellow-Green #2"),
                    ("#cde699", "Yellow-Green #3"),
                    ("#c2e184", "Yellow-Green #4"),
                    ("#b8dc70", "Yellow-Green #5"),
                    ("#aed75b", "Yellow-Green #6"),
                    ("#a4d247", "Yellow-Green #7"),
                    ("#9acd32", "Yellow-Green #8"),
                    ("#8bb92d", "Yellow-Green #9"),
                    ("#7ba428", "Yellow-Green #10"),
                    ("#6c9023", "Yellow-Green #11"),
                    ("#5c7b1e", "Yellow-Green #12"),
                    ("#4d6719", "Yellow-Green #13"),
                    ("#3e5214", "Yellow-Green #14"),
                    ("#2e3d0f", "Yellow-Green #15"),
                    ("#b3ffb3", "Green #1"),
                    ("#99ff99", "Green #2"),
                    ("#80ff80", "Green #3"),
                    ("#66ff66", "Green #4"),
                    ("#4dff4d", "Green #5"),
                    ("#33ff33", "Green #6"),
                    ("#1aff1a", "Green #7"),
                    ("#00ff00", "Green #8"),
                    ("#00e600", "Green #9"),
                    ("#00cc00", "Green #10"),
                    ("#00b300", "Green #11"),
                    ("#009900", "Green #12"),
                    ("#008000", "Green #13"),
                    ("#006600", "Green #14"),
                    ("#004c00", "Green #15"),
                    ("#b6e0ea", "Blue-Green #1"),
                    ("#9ed6e3", "Blue-Green #2"),
                    ("#86ccdd", "Blue-Green #3"),
                    ("#6ec1d6", "Blue-Green #4"),
                    ("#56b7cf", "Blue-Green #5"),
                    ("#3dadc8", "Blue-Green #6"),
                    ("#25a2c1", "Blue-Green #7"),
                    ("#0d98ba", "Blue-Green #8"),
                    ("#0c89a7", "Blue-Green #9"),
                    ("#0a7a95", "Blue-Green #10"),
                    ("#096a82", "Blue-Green #11"),
                    ("#085b70", "Blue-Green #12"),
                    ("#074c5d", "Blue-Green #13"),
                    ("#053d4a", "Blue-Green #14"),
                    ("#042e38", "Blue-Green #15"),
                    ("#b3b3ff", "Blue #1"),
                    ("#9999ff", "Blue #2"),
                    ("#8080ff", "Blue #3"),
                    ("#6666ff", "Blue #4"),
                    ("#4d4dff", "Blue #5"),
                    ("#3333ff", "Blue #6"),
                    ("#1a1aff", "Blue #7"),
                    ("#0000ff", "Blue #8"),
                    ("#0000e6", "Blue #9"),
                    ("#0000cc", "Blue #10"),
                    ("#0000b3", "Blue #11"),
                    ("#000099", "Blue #12"),
                    ("#000080", "Blue #13"),
                    ("#000066", "Blue #14"),
                    ("#00004c", "Blue #15"),
                    ("#dcbff6", "Blue-Violet #1"),
                    ("#d0aaf3", "Blue-Violet #2"),
                    ("#c595f1", "Blue-Violet #3"),
                    ("#b980ee", "Blue-Violet #4"),
                    ("#ad6beb", "Blue-Violet #5"),
                    ("#a155e8", "Blue-Violet #6"),
                    ("#9640e5", "Blue-Violet #7"),
                    ("#8a2be2", "Blue-Violet #8"),
                    ("#7c27cb", "Blue-Violet #9"),
                    ("#6e22b5", "Blue-Violet #10"),
                    ("#611e9e", "Blue-Violet #11"),
                    ("#531a88", "Blue-Violet #12"),
                    ("#451671", "Blue-Violet #13"),
                    ("#37115a", "Blue-Violet #14"),
                    ("#290d44", "Blue-Violet #15"),
                    ("#d9b3ff", "Violet #1"),
                    ("#cc99ff", "Violet #2"),
                    ("#bf80ff", "Violet #3"),
                    ("#b266ff", "Violet #4"),
                    ("#a54dff", "Violet #5"),
                    ("#9933ff", "Violet #6"),
                    ("#8c1aff", "Violet #7"),
                    ("#7f00ff", "Violet #8"),
                    ("#7200e6", "Violet #9"),
                    ("#6600cc", "Violet #10"),
                    ("#5900b3", "Violet #11"),
                    ("#4c0099", "Violet #12"),
                    ("#400080", "Violet #13"),
                    ("#330066", "Violet #14"),
                    ("#26004c", "Violet #15"),
                    ("#debfc5", "Red-Violet #1"),
                    ("#d3aab2", "Red-Violet #2"),
                    ("#c9959f", "Red-Violet #3"),
                    ("#be808b", "Red-Violet #4"),
                    ("#b36b78", "Red-Violet #5"),
                    ("#a85565", "Red-Violet #6"),
                    ("#9d4051", "Red-Violet #7"),
                    ("#922b3e", "Red-Violet #8"),
                    ("#832738", "Red-Violet #9"),
                    ("#752232", "Red-Violet #10"),
                    ("#661e2b", "Red-Violet #11"),
                    ("#581a25", "Red-Violet #12"),
                    ("#49161f", "Red-Violet #13"),
                    ("#3a1119", "Red-Violet #14"),
                    ("#2c0d13", "Red-Violet #15"),
                    ("#f7f5f0", "White #1"),
                    ("#deddd8", "Grey #1"),
                    ("#c6c4c0", "Grey #2"),
                    ("#adaca8", "Grey #3"),
                    ("#949390", "Grey #4"),
                    ("#7c7b78", "Grey #5"),
                    ("#313130", "Black #1"),
                    ("#191818", "Black #2"),
                    ("#c09366", "Brown #1"),
                    ("#b6814d", "Brown #2"),
                    ("#ab6f33", "Brown #3"),
                    ("#a15d1a", "Brown #4"),
                    ("#964b00", "Brown #5"),
                    ("#874400", "Brown #6"),
                    ("#783c00", "Brown #7"),
                    ("#693500", "Brown #8"),
                    ("#5a2d00", "Brown #9"),
                    ("#4b2600", "Brown #10"),
                ],
                default=("#ffb3b3", "Red #1"),
                max_length=17,
            ),
        ),
        migrations.AlterField(
            model_name="shoe",
            name="colour",
            field=models.CharField(
                choices=[
                    ("#ffb3b3", "Red #1"),
                    ("#ff9999", "Red #2"),
                    ("#ff8080", "Red #3"),
                    ("#ff6666", "Red #4"),
                    ("#ff4d4d", "Red #5"),
                    ("#ff3333", "Red #6"),
                    ("#ff1a1a", "Red #7"),
                    ("#ff0000", "Red #8"),
                    ("#e60000", "Red #9"),
                    ("#cc0000", "Red #10"),
                    ("#b30000", "Red #11"),
                    ("#990000", "Red #12"),
                    ("#800000", "Red #13"),
                    ("#660000", "Red #14"),
                    ("#4c0000", "Red #15"),
                    ("#ffcbc8", "Red-Orange #1"),
                    ("#ffbab6", "Red-Orange #2"),
                    ("#ffa9a4", "Red-Orange #3"),
                    ("#ff9892", "Red-Orange #4"),
                    ("#ff8780", "Red-Orange #5"),
                    ("#ff756d", "Red-Orange #6"),
                    ("#ff645b", "Red-Orange #7"),
                    ("#ff5349", "Red-Orange #8"),
                    ("#e64b42", "Red-Orange #9"),
                    ("#cc423a", "Red-Orange #10"),
                    ("#b33a33", "Red-Orange #11"),
                    ("#99322c", "Red-Orange #12"),
                    ("#802a25", "Red-Orange #13"),
                    ("#66211d", "Red-Orange #14"),
                    ("#4c1916", "Red-Orange #15"),
                    ("#ffe4b3", "Orange #1"),
                    ("#ffdb99", "Orange #2"),
                    ("#ffd280", "Orange #3"),
                    ("#ffc966", "Orange #4"),
                    ("#ffc04d", "Orange #5"),
                    ("#ffb733", "Orange #6"),
                    ("#ffae1a", "Orange #7"),
                    ("#ffa500", "Orange #8"),
                    ("#e69500", "Orange #9"),
                    ("#cc8400", "Orange #10"),
                    ("#fcebbc", "Yellow-Orange #1"),
                    ("#fbe5a5", "Yellow-Orange #2"),
                    ("#fade8f", "Yellow-Orange #3"),
                    ("#f9d779", "Yellow-Orange #4"),
                    ("#f8d162", "Yellow-Orange #5"),
                    ("#f7ca4c", "Yellow-Orange #6"),
                    ("#f6c435", "Yellow-Orange #7"),
                    ("#f5bd1f", "Yellow-Orange #8"),
                    ("#ddaa1c", "Yellow-Orange #9"),
                    ("#c49719", "Yellow-Orange #10"),
                    ("#ac8416", "Yellow-Orange #11"),
                    ("#937113", "Yellow-Orange #12"),
                    ("#7b5f10", "Yellow-Orange #13"),
                    ("#624c0c", "Yellow-Orange #14"),
                    ("#493909", "Yellow-Orange #15"),
                    ("#ffffb3", "Yellow #1"),
                    ("#ffff99", "Yellow #2"),
                    ("#ffff80", "Yellow #3"),
                    ("#ffff66", "Yellow #4"),
                    ("#ffff4d", "Yellow #5"),
                    ("#ffff33", "Yellow #6"),
                    ("#ffff1a", "Yellow #7"),
                    ("#ffff00", "Yellow #8"),
                    ("#e6e600", "Yellow #9"),
                    ("#cccc00", "Yellow #10"),
                    ("#b3b300", "Yellow #11"),
                    ("#999900", "Yellow #12"),
                    ("#808000", "Yellow #13"),
                    ("#666600", "Yellow #14"),
                    ("#4c4c00", "Yellow #15"),
                    ("#e1f0c2", "Yellow-Green #1"),
                    ("#d7ebad", "Yellow-Green #2"),
                    ("#cde699", "Yellow-Green #3"),
                    ("#c2e184", "Yellow-Green #4"),
                    ("#b8dc70", "Yellow-Green #5"),
                    ("#aed75b", "Yellow-Green #6"),
                    ("#a4d247", "Yellow-Green #7"),
                    ("#9acd32", "Yellow-Green #8"),
                    ("#8bb92d", "Yellow-Green #9"),
                    ("#7ba428", "Yellow-Green #10"),
                    ("#6c9023", "Yellow-Green #11"),
                    ("#5c7b1e", "Yellow-Green #12"),
                    ("#4d6719", "Yellow-Green #13"),
                    ("#3e5214", "Yellow-Green #14"),
                    ("#2e3d0f", "Yellow-Green #15"),
                    ("#b3ffb3", "Green #1"),
                    ("#99ff99", "Green #2"),
                    ("#80ff80", "Green #3"),
                    ("#66ff66", "Green #4"),
                    ("#4dff4d", "Green #5"),
                    ("#33ff33", "Green #6"),
                    ("#1aff1a", "Green #7"),
                    ("#00ff00", "Green #8"),
                    ("#00e600", "Green #9"),
                    ("#00cc00", "Green #10"),
                    ("#00b300", "Green #11"),
                    ("#009900", "Green #12"),
                    ("#008000", "Green #13"),
                    ("#006600", "Green #14"),
                    ("#004c00", "Green #15"),
                    ("#b6e0ea", "Blue-Green #1"),
                    ("#9ed6e3", "Blue-Green #2"),
                    ("#86ccdd", "Blue-Green #3"),
                    ("#6ec1d6", "Blue-Green #4"),
                    ("#56b7cf", "Blue-Green #5"),
                    ("#3dadc8", "Blue-Green #6"),
                    ("#25a2c1", "Blue-Green #7"),
                    ("#0d98ba", "Blue-Green #8"),
                    ("#0c89a7", "Blue-Green #9"),
                    ("#0a7a95", "Blue-Green #10"),
                    ("#096a82", "Blue-Green #11"),
                    ("#085b70", "Blue-Green #12"),
                    ("#074c5d", "Blue-Green #13"),
                    ("#053d4a", "Blue-Green #14"),
                    ("#042e38", "Blue-Green #15"),
                    ("#b3b3ff", "Blue #1"),
                    ("#9999ff", "Blue #2"),
                    ("#8080ff", "Blue #3"),
                    ("#6666ff", "Blue #4"),
                    ("#4d4dff", "Blue #5"),
                    ("#3333ff", "Blue #6"),
                    ("#1a1aff", "Blue #7"),
                    ("#0000ff", "Blue #8"),
                    ("#0000e6", "Blue #9"),
                    ("#0000cc", "Blue #10"),
                    ("#0000b3", "Blue #11"),
                    ("#000099", "Blue #12"),
                    ("#000080", "Blue #13"),
                    ("#000066", "Blue #14"),
                    ("#00004c", "Blue #15"),
                    ("#dcbff6", "Blue-Violet #1"),
                    ("#d0aaf3", "Blue-Violet #2"),
                    ("#c595f1", "Blue-Violet #3"),
                    ("#b980ee", "Blue-Violet #4"),
                    ("#ad6beb", "Blue-Violet #5"),
                    ("#a155e8", "Blue-Violet #6"),
                    ("#9640e5", "Blue-Violet #7"),
                    ("#8a2be2", "Blue-Violet #8"),
                    ("#7c27cb", "Blue-Violet #9"),
                    ("#6e22b5", "Blue-Violet #10"),
                    ("#611e9e", "Blue-Violet #11"),
                    ("#531a88", "Blue-Violet #12"),
                    ("#451671", "Blue-Violet #13"),
                    ("#37115a", "Blue-Violet #14"),
                    ("#290d44", "Blue-Violet #15"),
                    ("#d9b3ff", "Violet #1"),
                    ("#cc99ff", "Violet #2"),
                    ("#bf80ff", "Violet #3"),
                    ("#b266ff", "Violet #4"),
                    ("#a54dff", "Violet #5"),
                    ("#9933ff", "Violet #6"),
                    ("#8c1aff", "Violet #7"),
                    ("#7f00ff", "Violet #8"),
                    ("#7200e6", "Violet #9"),
                    ("#6600cc", "Violet #10"),
                    ("#5900b3", "Violet #11"),
                    ("#4c0099", "Violet #12"),
                    ("#400080", "Violet #13"),
                    ("#330066", "Violet #14"),
                    ("#26004c", "Violet #15"),
                    ("#debfc5", "Red-Violet #1"),
                    ("#d3aab2", "Red-Violet #2"),
                    ("#c9959f", "Red-Violet #3"),
                    ("#be808b", "Red-Violet #4"),
                    ("#b36b78", "Red-Violet #5"),
                    ("#a85565", "Red-Violet #6"),
                    ("#9d4051", "Red-Violet #7"),
                    ("#922b3e", "Red-Violet #8"),
                    ("#832738", "Red-Violet #9"),
                    ("#752232", "Red-Violet #10"),
                    ("#661e2b", "Red-Violet #11"),
                    ("#581a25", "Red-Violet #12"),
                    ("#49161f", "Red-Violet #13"),
                    ("#3a1119", "Red-Violet #14"),
                    ("#2c0d13", "Red-Violet #15"),
                    ("#f7f5f0", "White #1"),
                    ("#deddd8", "Grey #1"),
                    ("#c6c4c0", "Grey #2"),
                    ("#adaca8", "Grey #3"),
                    ("#949390", "Grey #4"),
                    ("#7c7b78", "Grey #5"),
                    ("#313130", "Black #1"),
                    ("#191818", "Black #2"),
                    ("#c09366", "Brown #1"),
                    ("#b6814d", "Brown #2"),
                    ("#ab6f33", "Brown #3"),
                    ("#a15d1a", "Brown #4"),
                    ("#964b00", "Brown #5"),
                    ("#874400", "Brown #6"),
                    ("#783c00", "Brown #7"),
                    ("#693500", "Brown #8"),
                    ("#5a2d00", "Brown #9"),
                    ("#4b2600", "Brown #10"),
                ],
                default=("#ffb3b3", "Red #1"),
                max_length=17,
            ),
        ),
        migrations.AlterField(
            model_name="topclothing",
            name="colour",
            field=models.CharField(
                choices=[
                    ("#ffb3b3", "Red #1"),
                    ("#ff9999", "Red #2"),
                    ("#ff8080", "Red #3"),
                    ("#ff6666", "Red #4"),
                    ("#ff4d4d", "Red #5"),
                    ("#ff3333", "Red #6"),
                    ("#ff1a1a", "Red #7"),
                    ("#ff0000", "Red #8"),
                    ("#e60000", "Red #9"),
                    ("#cc0000", "Red #10"),
                    ("#b30000", "Red #11"),
                    ("#990000", "Red #12"),
                    ("#800000", "Red #13"),
                    ("#660000", "Red #14"),
                    ("#4c0000", "Red #15"),
                    ("#ffcbc8", "Red-Orange #1"),
                    ("#ffbab6", "Red-Orange #2"),
                    ("#ffa9a4", "Red-Orange #3"),
                    ("#ff9892", "Red-Orange #4"),
                    ("#ff8780", "Red-Orange #5"),
                    ("#ff756d", "Red-Orange #6"),
                    ("#ff645b", "Red-Orange #7"),
                    ("#ff5349", "Red-Orange #8"),
                    ("#e64b42", "Red-Orange #9"),
                    ("#cc423a", "Red-Orange #10"),
                    ("#b33a33", "Red-Orange #11"),
                    ("#99322c", "Red-Orange #12"),
                    ("#802a25", "Red-Orange #13"),
                    ("#66211d", "Red-Orange #14"),
                    ("#4c1916", "Red-Orange #15"),
                    ("#ffe4b3", "Orange #1"),
                    ("#ffdb99", "Orange #2"),
                    ("#ffd280", "Orange #3"),
                    ("#ffc966", "Orange #4"),
                    ("#ffc04d", "Orange #5"),
                    ("#ffb733", "Orange #6"),
                    ("#ffae1a", "Orange #7"),
                    ("#ffa500", "Orange #8"),
                    ("#e69500", "Orange #9"),
                    ("#cc8400", "Orange #10"),
                    ("#fcebbc", "Yellow-Orange #1"),
                    ("#fbe5a5", "Yellow-Orange #2"),
                    ("#fade8f", "Yellow-Orange #3"),
                    ("#f9d779", "Yellow-Orange #4"),
                    ("#f8d162", "Yellow-Orange #5"),
                    ("#f7ca4c", "Yellow-Orange #6"),
                    ("#f6c435", "Yellow-Orange #7"),
                    ("#f5bd1f", "Yellow-Orange #8"),
                    ("#ddaa1c", "Yellow-Orange #9"),
                    ("#c49719", "Yellow-Orange #10"),
                    ("#ac8416", "Yellow-Orange #11"),
                    ("#937113", "Yellow-Orange #12"),
                    ("#7b5f10", "Yellow-Orange #13"),
                    ("#624c0c", "Yellow-Orange #14"),
                    ("#493909", "Yellow-Orange #15"),
                    ("#ffffb3", "Yellow #1"),
                    ("#ffff99", "Yellow #2"),
                    ("#ffff80", "Yellow #3"),
                    ("#ffff66", "Yellow #4"),
                    ("#ffff4d", "Yellow #5"),
                    ("#ffff33", "Yellow #6"),
                    ("#ffff1a", "Yellow #7"),
                    ("#ffff00", "Yellow #8"),
                    ("#e6e600", "Yellow #9"),
                    ("#cccc00", "Yellow #10"),
                    ("#b3b300", "Yellow #11"),
                    ("#999900", "Yellow #12"),
                    ("#808000", "Yellow #13"),
                    ("#666600", "Yellow #14"),
                    ("#4c4c00", "Yellow #15"),
                    ("#e1f0c2", "Yellow-Green #1"),
                    ("#d7ebad", "Yellow-Green #2"),
                    ("#cde699", "Yellow-Green #3"),
                    ("#c2e184", "Yellow-Green #4"),
                    ("#b8dc70", "Yellow-Green #5"),
                    ("#aed75b", "Yellow-Green #6"),
                    ("#a4d247", "Yellow-Green #7"),
                    ("#9acd32", "Yellow-Green #8"),
                    ("#8bb92d", "Yellow-Green #9"),
                    ("#7ba428", "Yellow-Green #10"),
                    ("#6c9023", "Yellow-Green #11"),
                    ("#5c7b1e", "Yellow-Green #12"),
                    ("#4d6719", "Yellow-Green #13"),
                    ("#3e5214", "Yellow-Green #14"),
                    ("#2e3d0f", "Yellow-Green #15"),
                    ("#b3ffb3", "Green #1"),
                    ("#99ff99", "Green #2"),
                    ("#80ff80", "Green #3"),
                    ("#66ff66", "Green #4"),
                    ("#4dff4d", "Green #5"),
                    ("#33ff33", "Green #6"),
                    ("#1aff1a", "Green #7"),
                    ("#00ff00", "Green #8"),
                    ("#00e600", "Green #9"),
                    ("#00cc00", "Green #10"),
                    ("#00b300", "Green #11"),
                    ("#009900", "Green #12"),
                    ("#008000", "Green #13"),
                    ("#006600", "Green #14"),
                    ("#004c00", "Green #15"),
                    ("#b6e0ea", "Blue-Green #1"),
                    ("#9ed6e3", "Blue-Green #2"),
                    ("#86ccdd", "Blue-Green #3"),
                    ("#6ec1d6", "Blue-Green #4"),
                    ("#56b7cf", "Blue-Green #5"),
                    ("#3dadc8", "Blue-Green #6"),
                    ("#25a2c1", "Blue-Green #7"),
                    ("#0d98ba", "Blue-Green #8"),
                    ("#0c89a7", "Blue-Green #9"),
                    ("#0a7a95", "Blue-Green #10"),
                    ("#096a82", "Blue-Green #11"),
                    ("#085b70", "Blue-Green #12"),
                    ("#074c5d", "Blue-Green #13"),
                    ("#053d4a", "Blue-Green #14"),
                    ("#042e38", "Blue-Green #15"),
                    ("#b3b3ff", "Blue #1"),
                    ("#9999ff", "Blue #2"),
                    ("#8080ff", "Blue #3"),
                    ("#6666ff", "Blue #4"),
                    ("#4d4dff", "Blue #5"),
                    ("#3333ff", "Blue #6"),
                    ("#1a1aff", "Blue #7"),
                    ("#0000ff", "Blue #8"),
                    ("#0000e6", "Blue #9"),
                    ("#0000cc", "Blue #10"),
                    ("#0000b3", "Blue #11"),
                    ("#000099", "Blue #12"),
                    ("#000080", "Blue #13"),
                    ("#000066", "Blue #14"),
                    ("#00004c", "Blue #15"),
                    ("#dcbff6", "Blue-Violet #1"),
                    ("#d0aaf3", "Blue-Violet #2"),
                    ("#c595f1", "Blue-Violet #3"),
                    ("#b980ee", "Blue-Violet #4"),
                    ("#ad6beb", "Blue-Violet #5"),
                    ("#a155e8", "Blue-Violet #6"),
                    ("#9640e5", "Blue-Violet #7"),
                    ("#8a2be2", "Blue-Violet #8"),
                    ("#7c27cb", "Blue-Violet #9"),
                    ("#6e22b5", "Blue-Violet #10"),
                    ("#611e9e", "Blue-Violet #11"),
                    ("#531a88", "Blue-Violet #12"),
                    ("#451671", "Blue-Violet #13"),
                    ("#37115a", "Blue-Violet #14"),
                    ("#290d44", "Blue-Violet #15"),
                    ("#d9b3ff", "Violet #1"),
                    ("#cc99ff", "Violet #2"),
                    ("#bf80ff", "Violet #3"),
                    ("#b266ff", "Violet #4"),
                    ("#a54dff", "Violet #5"),
                    ("#9933ff", "Violet #6"),
                    ("#8c1aff", "Violet #7"),
                    ("#7f00ff", "Violet #8"),
                    ("#7200e6", "Violet #9"),
                    ("#6600cc", "Violet #10"),
                    ("#5900b3", "Violet #11"),
                    ("#4c0099", "Violet #12"),
                    ("#400080", "Violet #13"),
                    ("#330066", "Violet #14"),
                    ("#26004c", "Violet #15"),
                    ("#debfc5", "Red-Violet #1"),
                    ("#d3aab2", "Red-Violet #2"),
                    ("#c9959f", "Red-Violet #3"),
                    ("#be808b", "Red-Violet #4"),
                    ("#b36b78", "Red-Violet #5"),
                    ("#a85565", "Red-Violet #6"),
                    ("#9d4051", "Red-Violet #7"),
                    ("#922b3e", "Red-Violet #8"),
                    ("#832738", "Red-Violet #9"),
                    ("#752232", "Red-Violet #10"),
                    ("#661e2b", "Red-Violet #11"),
                    ("#581a25", "Red-Violet #12"),
                    ("#49161f", "Red-Violet #13"),
                    ("#3a1119", "Red-Violet #14"),
                    ("#2c0d13", "Red-Violet #15"),
                    ("#f7f5f0", "White #1"),
                    ("#deddd8", "Grey #1"),
                    ("#c6c4c0", "Grey #2"),
                    ("#adaca8", "Grey #3"),
                    ("#949390", "Grey #4"),
                    ("#7c7b78", "Grey #5"),
                    ("#313130", "Black #1"),
                    ("#191818", "Black #2"),
                    ("#c09366", "Brown #1"),
                    ("#b6814d", "Brown #2"),
                    ("#ab6f33", "Brown #3"),
                    ("#a15d1a", "Brown #4"),
                    ("#964b00", "Brown #5"),
                    ("#874400", "Brown #6"),
                    ("#783c00", "Brown #7"),
                    ("#693500", "Brown #8"),
                    ("#5a2d00", "Brown #9"),
                    ("#4b2600", "Brown #10"),
                ],
                default=("#ffb3b3", "Red #1"),
                max_length=17,
            ),
        ),
    ]