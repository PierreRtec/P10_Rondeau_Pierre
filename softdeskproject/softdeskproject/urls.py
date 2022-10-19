from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from softdeskapp.views import ProjectsViewSet, IssuesViewSet, CommentsViewSet, ContributorsViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectsViewSet, basename="projects")
# {url}projects/id/contributor
# id dans le router

project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'contributors', ContributorsViewSet, basename="projects")
project_router.register(r'issues', IssuesViewSet, basename="issues")
project_router.register(r'comments', CommentsViewSet, basename="comments")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/login/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("auth/login/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("api/", include(router.urls)),
    path('api/', include(project_router.urls)),
]

