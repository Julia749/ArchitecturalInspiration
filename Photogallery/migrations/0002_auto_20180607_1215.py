# Generated by Django 2.0.6

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photogallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ArchitecturalStyle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
