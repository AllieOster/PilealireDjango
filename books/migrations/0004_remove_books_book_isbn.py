# Generated by Django 4.2.7 on 2023-11-21 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_books_couverture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book_isbn',
        ),
    ]