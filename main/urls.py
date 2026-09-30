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
    get_projects_json,      
    create_project_ajax,    
    register,
    login_user,
    logout_user,
    toggle_star,
)

app_name = "main"

urlpatterns = [
    # Main / Profile Page
    path("", show_main, name="show_main"),
    
    # Project URLs
    path("projects/", show_project, name="show_project"),
    path("projects/json/", get_projects_json, name="get_projects_json"),     # Endpoint AJAX Get Data
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"), # Endpoint AJAX Add Data
    path("projects/create/", create_project, name="create_project"),
    path("projects/<uuid:id>/edit/", edit_project, name="edit_project"),
    path("projects/<uuid:id>/delete/", delete_project, name="delete_project"),
    path("projects/<uuid:id>/star/", toggle_star, name="toggle_star"),
    path("json/", show_json, name="show_json"),
    
    # Experience URLs
    path("experience/", show_experience, name="show_experience"),
    path("experience/create/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("experience/json/", show_experience_json, name="show_experience_json"),

    # Authentication URLs
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]