
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Main website
    path("", include("main.urls")),

    # Contacts
    path("contacts/", include("contacts.urls")),

    # Project API - Tutorial 07
    path("api/", include("main.project_api_urls")),

    # Experience API - Tugas 6
    path("api/v1/", include("main.api_urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
