# Generated by Django 4.2.4 on 2023-09-16 02:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("visitantes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="visitor",
            old_name="left_time",
            new_name="leave_time",
        ),
    ]
