# Generated by Django 4.1.2 on 2022-10-16 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("softdeskapp", "0003_alter_projects_type_contributors"),
    ]

    operations = [
        migrations.CreateModel(
            name="Issues",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("desc", models.CharField(max_length=1024)),
                ("tag", models.CharField(max_length=24)),
                ("priority", models.CharField(max_length=24)),
                ("created_time", models.DateTimeField(verbose_name="Date")),
                (
                    "issue_author_user_id",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issue_author_admin",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "issue_user",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issue_contrib_admin",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment_id", models.IntegerField()),
                ("description", models.CharField(max_length=1024)),
                ("tag", models.CharField(max_length=24)),
                ("priority", models.CharField(max_length=24)),
                ("created_time", models.DateTimeField(verbose_name="Date")),
                (
                    "comment_author_user_id",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_admin",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "comment_issue_id",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issue_id_admin",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]