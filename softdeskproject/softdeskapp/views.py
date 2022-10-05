from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Users
from .serializers import UsersSerializer


class UsersViewset(ReadOnlyModelViewSet):

    serializer_class = UsersSerializer

    def get_queryset(self):
        return Users(active=True)
