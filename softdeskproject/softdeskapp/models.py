from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

TYPES_PROJECTS = [("A", 'typeA'), ("B", 'typeB'), ("C", 'typeC')]


class Projects(models.Model):

    objects = None
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    type = models.CharField(max_length=10, choices=TYPES_PROJECTS)
    author_user = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="project_admin",
        on_delete=models.CASCADE,
        blank=True
    )

    def __str__(self):
        return self.title


class Contributors(models.Model):

    objects = None

    contrib_user = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="contrib_admin",
        on_delete=models.CASCADE,
        blank=True
    )
    project_id = models.ForeignKey(
        to=Projects,
        related_name="project_admin",
        on_delete=models.CASCADE,
        blank=True
    )

    def __str__(self):
        return self.contrib_user


class Issues(models.Model):

    objects = None

    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=1024)
    tag = models.CharField(max_length=24)
    priority = models.CharField(max_length=24)
    issue_author_user_id = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="issue_author_admin",
        on_delete=models.CASCADE,
        blank=True
    )
    issue_user = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="issue_contrib_admin",
        on_delete=models.CASCADE,
        blank=True
    )
    created_time = models.DateTimeField(verbose_name="Date")

    def __str__(self):
        return self.title


class Comments(models.Model):

    objects = None

    comment_id = models.IntegerField()
    description = models.CharField(max_length=1024)
    tag = models.CharField(max_length=24)
    priority = models.CharField(max_length=24)
    comment_author_user_id = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="comment_admin",
        on_delete=models.CASCADE,
        blank=True
    )
    comment_issue_id = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="issue_id_admin",
        on_delete=models.CASCADE,
        blank=True
    )
    created_time = models.DateTimeField(verbose_name="Date")

    def __str__(self):
        return self.comment_id
