# Generated by Django 5.1.1 on 2024-10-03 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, null=True, to='main.ingredient'),
        ),
    ]
