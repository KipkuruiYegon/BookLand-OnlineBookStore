# Generated by Django 3.2.23 on 2023-11-29 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshopstore', '0006_alter_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=0, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='bookshopstore.category'),
        ),
    ]
