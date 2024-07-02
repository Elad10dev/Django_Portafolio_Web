# Generated by Django 5.0.6 on 2024-07-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketApp', '0003_alter_itemdb_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemdb',
            name='image_url',
        ),
        migrations.AddField(
            model_name='itemdb',
            name='image',
            field=models.ImageField(null=True, upload_to='items/'),
        ),
    ]
