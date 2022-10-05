from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from softdeskapp.views import UsersViewset

router = routers.SimpleRouter()
router.register("users", UsersViewset, basename="users")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/', include(router.urls))
]