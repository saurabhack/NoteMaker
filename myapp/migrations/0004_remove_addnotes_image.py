# Generated by Django 3.2.12 on 2023-07-19 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_addnote_addnotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addnotes',
            name='image',
        ),
    ]