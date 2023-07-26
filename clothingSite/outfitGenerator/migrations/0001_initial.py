# Generated by Django 4.1.7 on 2023-06-21 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BottomClothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(choices=[('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('YG', 'Yellow-Green'), ('G', 'Green'), ('BG', 'Blue-Green'), ('B', 'BLUE'), ('BV', 'Blue-Violet'), ('V', 'Violet'), ('M', 'Mauve'), ('MP', 'Mauve-Pink'), ('P', 'Pink')], default='R', max_length=2)),
                ('type', models.CharField(choices=[('TS', 'T-Shirt'), ('DS', 'Dress Shirt'), ('J', 'Jacket')], default='TS', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(choices=[('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('YG', 'Yellow-Green'), ('G', 'Green'), ('BG', 'Blue-Green'), ('B', 'BLUE'), ('BV', 'Blue-Violet'), ('V', 'Violet'), ('M', 'Mauve'), ('MP', 'Mauve-Pink'), ('P', 'Pink')], default='R', max_length=2)),
                ('type', models.CharField(choices=[('S', 'Sneakers'), ('DS', 'Dress Shoes'), ('RS', 'Running Shoes')], default='S', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TopClothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(choices=[('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('YG', 'Yellow-Green'), ('G', 'Green'), ('BG', 'Blue-Green'), ('B', 'BLUE'), ('BV', 'Blue-Violet'), ('V', 'Violet'), ('M', 'Mauve'), ('MP', 'Mauve-Pink'), ('P', 'Pink')], default='R', max_length=2)),
                ('type', models.CharField(choices=[('TS', 'T-Shirt'), ('DS', 'Dress Shirt'), ('J', 'Jacket')], default='TS', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]