# Generated by Django 4.1.2 on 2022-10-19 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("softdeskapp", "0004_issues_comments"),
    ]

    operations = [
        migrations.RenameField(
            model_name="projects",
            old_name="author_user_id",
            new_name="author_user",
        ),
    ]
