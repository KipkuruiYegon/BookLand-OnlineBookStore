# Generated by Django 3.2.23 on 2023-11-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshopstore', '0007_alter_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='on_sale',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
