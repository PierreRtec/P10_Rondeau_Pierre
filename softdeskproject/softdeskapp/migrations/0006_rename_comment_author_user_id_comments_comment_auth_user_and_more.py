# Generated by Django 4.1.2 on 2022-11-03 12:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("softdeskapp", "0005_rename_author_user_id_projects_author_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comments",
            old_name="comment_author_user_id",
            new_name="comment_auth_user",
        ),
        migrations.RemoveField(
            model_name="comments",
            name="comment_id",
        ),
        migrations.RemoveField(
            model_name="comments",
            name="comment_issue_id",
        ),
        migrations.RemoveField(
            model_name="issues",
            name="issue_author_user_id",
        ),
        migrations.RemoveField(
            model_name="issues",
            name="issue_user",
        ),
        migrations.AddField(
            model_name="comments",
            name="comment_issue",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issue_comment_admin",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="issues",
            name="assignee",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assignee_admin",
                to="softdeskapp.contributors",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="issues",
            name="author",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issue_admin",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="issues",
            name="project",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issue_project_admin",
                to="softdeskapp.projects",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="issues",
            name="status",
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AlterField(
            model_name="comments",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date"),
        ),
        migrations.AlterField(
            model_name="issues",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date"),
        ),
    ]
