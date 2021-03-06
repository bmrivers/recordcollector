# Generated by Django 2.1.5 on 2019-03-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20190313_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.CharField(choices=[('ALT', 'Alternative'), ('AMB', 'Ambient'), ('BLU', 'Blues'), ('CLA', 'Classical'), ('DIS', 'Disco'), ('EMO', 'Emo'), ('EXP', 'Experimental'), ('FOL', 'Folk'), ('FUN', 'Funk'), ('HOU', 'House'), ('IDT', 'Industrial'), ('IND', 'Indie'), ('MET', 'Metal'), ('PUN', 'Punk'), ('RAP', 'Rap'), ('REG', 'Reggae'), ('SKA', 'Ska'), ('SOT', 'Soundtrack'), ('SOU', 'Soul'), ('TEC', 'Techno')], default='ALT', max_length=20),
        ),
    ]
