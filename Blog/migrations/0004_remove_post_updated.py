# Generated by Django 5.0.2 on 2024-02-26 10:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Blog", "0003_alter_post_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="updated",
        ),
    ]