
from django.urls import path
from .views import (
    project_list_create_api,
    project_detail_api,
)

urlpatterns = [
    path(
        "projects/",
        project_list_create_api,
        name="project_list_create_api",
    ),
    path(
        "projects/<uuid:id>/",
        project_detail_api,
        name="project_detail_api",
    ),
]
