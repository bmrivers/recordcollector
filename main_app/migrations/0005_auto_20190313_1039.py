# Generated by Django 2.1.5 on 2019-03-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20190312_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('genre', models.CharField(choices=[('ALT', 'Alternative'), ('AMB', 'Ambient'), ('BLU', 'Blues'), ('CLA', 'Classical'), ('DIS', 'Disco'), ('EMO', 'Emo'), ('EXP', 'Experimental'), ('FOL', 'Folk'), ('FUN', 'Funk'), ('HOU', 'House'), ('IDT', 'Industrial'), ('IND', 'Indie'), ('MET', 'Metal'), ('PUN', 'Punk'), ('RAP', 'Rap'), ('REG', 'Reggae'), ('SKA', 'Ska'), ('SOT', 'Soundtrack'), ('SOU', 'Soul'), ('TEC', 'Techno')], default='Rock', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='artists',
            field=models.ManyToManyField(to='main_app.Artist'),
        ),
    ]
