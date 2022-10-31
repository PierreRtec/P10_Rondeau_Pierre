from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from softdeskapp.views import (
    CommentsViewSet,
    ContributorsViewSet,
    IssuesViewSet,
    ProjectsViewSet,
    RegisterViewSet,
)

router = routers.SimpleRouter()
router.register(r"projects", ProjectsViewSet, basename="projects")
router.register(r"register", RegisterViewSet, basename="register")
router.register(r"issues", RegisterViewSet, basename="issues")

project_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
project_router.register(r"contributors", ContributorsViewSet, basename="projects")
project_router.register(r"issues", IssuesViewSet, basename="issues")


issue_router = routers.NestedSimpleRouter(project_router, r"issues", lookup="issue")
issue_router.register(r"comments", CommentsViewSet, basename="comments")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/login/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("auth/login/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("api/", include(router.urls)),
    path("api/", include(project_router.urls)),
    path("api/", include(issue_router.urls)),
]
