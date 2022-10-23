from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Contributors, Issues, Projects
from .permissions import AuthorAccess, ContributorReadOnly
from .serializers import (ContributorsSerializer,
                          IssuesSerializer, ProjectsSerializer,
                          RegisterSerializer, User)

"""
ACCES ENDPOINT, PERMISSIONS, GESTION DE DONNEES, REQUETES
Les views sont là pour permettre l'accès à un endpoint (à ce qu'il renvoit)
ModelViewSet créé un CRUD de base
APIViewSet faut tout faire à la main, pas de routes de base
"""


class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.all()


class ProjectsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ContributorReadOnly, AuthorAccess]
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        queryset_auth_user = Projects.objects.filter(author_user=self.request.user) # attribut du modèle
        queryset_contrib_user = Projects.objects.filter(project_admin__contrib_user=self.request.user) # __ module descend dans le modèle / project_admin == related name
        return (queryset_auth_user | queryset_contrib_user).distinct()


class ContributorsViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorsSerializer
    permission_classes = [IsAuthenticated, ContributorReadOnly]

    def get_queryset(self):
        contributors = Contributors.objects.filter(project_id=self.kwargs['project_pk'])  # pk = primary_key =  nom du lookup dans le kwargs
        return contributors


class IssuesViewSet(viewsets.ModelViewSet):
    serializer_class = IssuesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project = Projects.objects.filter(author_user=self.request.user) # attribut du modèle
        issues = Issues.objects.filter(assignee_id=self.kwargs['project_pk'], project=project)
        return issues
