from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Projects, Contributors, Issues, Comments
from .permissions import ContributorReadOnly, AuthorAccess
from .serializers import ProjectsSerializer, CommentsSerializer, IssuesSerializer, ContributorsSerializer



"""
ACCES ENDPOINT, PERMISSIONS, GESTION DE DONNEES, REQUETES
Les views sont là pour permettre l'accès à un endpoint (à ce qu'il renvoit)
ModelViewSet créé un CRUD de base
APIViewSet faut tout faire à la main, pas de routes de base
"""


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

    def get_queryset(self):
        issues = Issues.objects.all()
        return issues


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        comments = Comments.objects.all()
        return comments

