from django.urls import path
from main.views import (
    show_main,
    show_experience,
    create_experience,
    edit_experience,
    delete_experience,
    show_experience_json,
    show_project,
    create_project,
    edit_project,
    delete_project,
    show_json,
)

app_name = "main"

urlpatterns = [
    # Main / Profile Page
    path("", show_main, name="show_main"),
    
    # Project URLs
    path("projects/", show_project, name="show_project"),
    path("projects/create/", create_project, name="create_project"),
    path("projects/<uuid:id>/edit/", edit_project, name="edit_project"),
    path("projects/<uuid:id>/delete/", delete_project, name="delete_project"),
    path("json/", show_json, name="show_json"),
    
    # Experience URLs
    path("experience/", show_experience, name="show_experience"),
    path("experience/create/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("experience/json/", show_experience_json, name="show_experience_json"),
]