# Generated by Django 4.2.7 on 2023-11-17 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='book_id',
            new_name='book_isbn',
        ),
    ]
