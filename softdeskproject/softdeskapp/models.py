from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

TAG = [("BUG", "bug"), ("AMELIORATION", "amélioration"), ("TACHE", "tâche")]
TYPES_PROJECTS = [("BACK", "back-end"), ("FRONT", "front-end"), ("IOS", "iOs"), ("ANDROID", "android")]
PRIORITY = [("ELEVEE", "élevée"), ("MOYENNE", "moyenne"), ("FAIBLE", "faible")]
STATUS = [("EN COURS", "en cours"), ("A FAIRE", "à faire"), ("TERMINEE", "terminée")]


class Projects(models.Model):

    objects = None
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    type = models.CharField(max_length=48, choices=TYPES_PROJECTS)
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
    tag = models.CharField(max_length=48, choices=TAG)
    priority = models.CharField(max_length=48, choices=PRIORITY)
    status = models.CharField(max_length=48, blank=True, choices=TYPES_PROJECTS)
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


class Comments(models.Model):

    objects = None

    description = models.CharField(max_length=1024)
    tag = models.CharField(max_length=48, choices=TAG)
    priority = models.CharField(max_length=48, choices=PRIORITY)
    comment_auth_user = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="comment_admin",
        on_delete=models.CASCADE,
        blank=True,
    )
    comment_issue = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="issue_comment_admin",
        on_delete=models.CASCADE,
        blank=True,
    )
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Date")

    def __str__(self):
        return self.tag
