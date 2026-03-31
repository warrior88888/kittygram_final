from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from cats.views import AchievementViewSet, CatViewSet
from config import app_config

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path(app_config.django.admin_path, admin.site.urls),
    path(app_config.django.healthcheck_path, include("health_check.urls")),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),  # Users management
    path('api/', include('djoser.urls.authtoken')),  # Token management
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
