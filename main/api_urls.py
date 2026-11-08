
from django.urls import path
from . import api_views
from .views import (
    project_list_create_api,
    project_detail_api,
)

app_name = "api"

urlpatterns = [
    # Experience API - Tugas 6
    path(
        "experiences/",
        api_views.experience_list_create_api,
        name="experience_list_create",
    ),
    path(
        "experiences/<uuid:pk>/",
        api_views.experience_detail_api,
        name="experience_detail",
    ),
    path(
        "experiences/<uuid:pk>/star/",
        api_views.experience_star_api,
        name="experience_star",
    ),

    # Project API - Tutorial 07
    path(
        "projects/",
        project_list_create_api,
        name="project_list_create",
    ),
    path(
        "projects/<uuid:id>/",
        project_detail_api,
        name="project_detail",
    ),
]
