# Generated by Django 4.1.2 on 2022-10-16 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("softdeskapp", "0002_projects_delete_choice_delete_question"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects",
            name="type",
            field=models.CharField(
                choices=[("A", "typeA"), ("B", "typeB"), ("C", "typeC")], max_length=10
            ),
        ),
        migrations.CreateModel(
            name="Contributors",
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
                (
                    "contrib_user",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contrib_admin",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_admin",
                        to="softdeskapp.projects",
                    ),
                ),
            ],
        ),
    ]