from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Contributors, Issues, Projects, Comments
from .permissions import IsAuthorProjectsView, IsAuthorContributorsView, IsAuthorContribIssue, IsAuthorContribComment
from .serializers import (ContributorsSerializer, CommentsSerializer,
                          IssuesSerializer, ProjectsSerializer,
                          RegisterSerializer, User)


class RegisterViewSet(viewsets.ModelViewSet):
    """
    Create user account when first connexion, registration view.
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.all()


class ProjectsViewSet(viewsets.ModelViewSet):
    """
    Projects view list
    perms : IsAuthenticated, IsOwnerProject
    """
    permission_classes = [IsAuthenticated, IsAuthorProjectsView]
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        queryset_auth_user = Projects.objects.filter(author_user=self.request.user)
        queryset_contrib_user = Projects.objects.filter(project_admin__contrib_user=self.request.user)
        return (queryset_auth_user | queryset_contrib_user).distinct()


class ContributorsViewSet(viewsets.ModelViewSet):
    """
    Contributors view list
    """
    serializer_class = ContributorsSerializer
    permission_classes = [IsAuthenticated, IsAuthorContributorsView]

    def get_queryset(self):
        contributors = Contributors.objects.filter(project_id=self.kwargs['project_pk'])
        return contributors


class IssuesViewSet(viewsets.ModelViewSet):
    """
    Issues view list
    """
    serializer_class = IssuesSerializer
    permission_classes = [IsAuthenticated, IsAuthorContribIssue]

    def get_queryset(self):
        issues = Issues.objects.filter(project=self.kwargs['project_pk'])
        return issues


class CommentsViewSet(viewsets.ModelViewSet):
    """
    Comments view list
    """
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, IsAuthorContribComment]

    def get_queryset(self):
        comments = Comments.objects.filter(comment_issue=self.kwargs['issue_pk'])
        return comments
