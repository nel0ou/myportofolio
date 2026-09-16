from django.urls import path
from main.views import (
    show_main,
    show_experience,
    show_project,
    create_project,
    delete_project,
    show_json,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("projects/", show_project, name="show_project"),
    path("projects/create/", create_project, name="create_project"),
    path("projects/<uuid:id>/delete/", delete_project, name="delete_project"),
    path("json/", show_json, name="show_json"),
]