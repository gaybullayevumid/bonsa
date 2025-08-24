from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
] + i18n_patterns(
    path("i18n/", include('django.conf.urls.i18n')),
    path("accounts/", include("apps.accounts.urls")),
    path("blog/", include("apps.blog.urls")),
    path("", include("apps.base.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)