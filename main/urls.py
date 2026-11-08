
from django.urls import path
from main.views import (
    # Main / Profile
    show_main,

    # Experience Views
    show_experience,
    create_experience,
    edit_experience,
    delete_experience,
    show_experience_json,
    create_experience_ajax,

    # Project Views
    show_project,
    create_project,
    edit_project,
    delete_project,
    show_json,
    get_projects_json,
    create_project_ajax,
    toggle_star,

    # Authentication Views
    register,
    login_user,
    logout_user,
)

app_name = "main"

urlpatterns = [
    # ==================== MAIN / PROFILE PAGE ====================
    path("", show_main, name="show_main"),

    # ==================== PROJECT URLs ====================
    path("projects/", show_project, name="show_project"),
    path("projects/json/", get_projects_json, name="get_projects_json"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("projects/create/", create_project, name="create_project"),
    path("projects/<uuid:id>/edit/", edit_project, name="edit_project"),
    path("projects/<uuid:id>/delete/", delete_project, name="delete_project"),
    path("projects/<uuid:id>/star/", toggle_star, name="toggle_star"),
    path("json/", show_json, name="show_json"),

    # ==================== EXPERIENCE URLs ====================
    path("experience/", show_experience, name="show_experience"),
    path("experience/json/", show_experience_json, name="show_experience_json"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("experience/create/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),

    # ==================== AUTHENTICATION URLs ====================
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
