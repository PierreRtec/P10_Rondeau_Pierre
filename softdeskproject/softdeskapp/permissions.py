from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

from .models import Comments, Contributors, Issues, Projects

"""CUSTOM PERMISSIONS"""


class IsAuthorProjectsView(permissions.BasePermission):
    """
    Check if user is author or contributor for project
    http_methods : destroy, update
    """
    def has_permission(self, request, view):
        if view.action in ("destroy", "update"):
            try:
                content = Projects.objects.get(pk=view.kwargs["pk"])
            except ObjectDoesNotExist:
                return False
            return content.author_user == request.user
        return True


class IsAuthorContributorsView(permissions.BasePermission):
    """
    Check if user is the contributor of the project
    http_methods : destroy, update
    """
    def has_permission(self, request, view):
        if view.action in ("destroy", "update"):
            try:
                content = Projects.objects.get(pk=view.kwargs["project_pk"])
            except ObjectDoesNotExist:
                return False
            return content.author_user == request.user
        return True


class IsAuthorContribIssue(permissions.BasePermission):
    """
    Check if user is author or contributor for a issue
    http_methods : list, retrieve, create
    """

    def has_permission(self, request, view):
        if view.action in ("list", "retrieve", "create"):
            try:
                project = Projects.objects.get(id=view.kwargs["project_pk"])
            except ObjectDoesNotExist:
                return False
            is_contrib_issue = Contributors.objects.filter(
                project_id=view.kwargs["project_pk"]
            ).filter(contrib_user=request.user.id)
            if project.author_user == request.user or bool(is_contrib_issue):
                return True
            return False
        if view.action in ("destroy", "update"):
            try:
                issue = Issues.objects.get(id=view.kwargs["pk"])
            except ObjectDoesNotExist:
                return False
            return issue.author == request.user


class IsAuthorContribComment(permissions.BasePermission):
    """
    Check if user is author or contributor for a comment
    http_methods : list, retrieve, create
    """

    def has_permission(self, request, view):
        if view.action in ("list", "retrieve", "create"):
            try:
                project = Projects.objects.get(id=view.kwargs["project_pk"])
            except ObjectDoesNotExist:
                return False
            is_contributor_comment = Contributors.objects.filter(
                project_id=view.kwargs["project_pk"]
            ).filter(contrib_user=request.user.id)

            if project.author_user == request.user or bool(is_contributor_comment):
                return True

        if view.action in ("destroy", "update"):
            try:
                comment = Comments.objects.get(id=view.kwargs["pk"])
            except ObjectDoesNotExist:
                return False
            return comment.comment_auth_user == request.user
        return False
