from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from softdeskapp.models import Contributors, Issues, Projects

"""
FORMATAGE DE LA DONNEE
Les serializers ne sont pas obligatoires
Il traite les données 
Quand on utilise un serializer, il gère et check les données valides
Il serialize le modèle, gestion modèle
On peut pas accèder aux données ici, ce sera dans la vue
"""


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"
        read_only_fields = ('author', 'id')

    def _user(self):
        request = self.context.get("request", None)
        if request:
            return request.user

    def create(self, validated_data):

        projects = Projects.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"],
            author_user=self._user(),
        )
        projects.save()

        return projects


class ContributorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = "__all__"

    def create(self, validated_data):
        project = Projects.objects.get(id=self.context["view"].kwargs["project_pk"])
        contributors = Contributors.objects.create(
            contrib_user=validated_data["contrib_user"], project_id=project
        )
        return contributors


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = "__all__"

    def create(self, validated_data):
        project = Projects.objects.get(id=self.context["view"].kwargs["project_pk"])
        issues = Issues.objects.create(
            assignee=validated_data["assignee"], project_id=project
        )
        return issues
