from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

TYPES_PROJECTS = [("A", "typeA"), ("B", "typeB"), ("C", "typeC")]


class Projects(models.Model):

    objects = None
    title = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=1024, unique=True)
    type = models.CharField(max_length=10, choices=TYPES_PROJECTS, unique=True)
    author_user = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="project_admin",
        on_delete=models.CASCADE,
        blank=True,
    )

    def __str__(self):
        return self.title


class Contributors(models.Model):

    objects = None

    contrib_user = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="contrib_admin",
        on_delete=models.CASCADE,
        blank=True,
    )
    project_id = models.ForeignKey(
        to=Projects, related_name="project_admin", on_delete=models.CASCADE, blank=True
    )

    def __str__(self):
        return self.contrib_user


class Issues(models.Model):

    objects = None

    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=1024)
    tag = models.CharField(max_length=24, unique=True)
    priority = models.CharField(max_length=24)
    status = models.CharField(max_length=24, blank=True)
    author = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="issue_admin",
        on_delete=models.CASCADE,
        blank=True,
    )
    project = models.ForeignKey(
        to=Projects, related_name="issue_project_admin", on_delete=models.CASCADE, blank=True
    )
    assignee = models.ForeignKey(
        to=Contributors, related_name="assignee_admin", on_delete=models.CASCADE, blank=True
    )
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Date")

#
# class Comments(models.Model):
#
#     objects = None
#
#     description = models.CharField(max_length=1024, unique=True)
#     tag = models.CharField(max_length=24, unique=True)
#     priority = models.CharField(max_length=24, unique=True)
#     comment_auth_user = models.ForeignKey(
#         to=AUTH_USER_MODEL,
#         related_name="comment_admin",
#         on_delete=models.CASCADE,
#         blank=True,
#     )
#     comment_issue = models.ForeignKey(
#         to=AUTH_USER_MODEL,
#         related_name="issue_comment_admin",
#         on_delete=models.CASCADE,
#         blank=True,
#     )
#     created_time = models.DateTimeField(verbose_name="Date")
#
#     def __str__(self):
#         return self.tag
