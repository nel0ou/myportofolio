
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.exceptions import PermissionDenied

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework import status

from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm
from main.serializers import ExperienceSerializer, ProjectSerializer


# ==================== HELPER ====================

def is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editor").exists()


# ==================== API PERMISSION ====================

class IsSuperuserOrReadOnly(BasePermission):
    """
    Semua pengguna boleh membaca data.
    Hanya superuser yang boleh mengubah data.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_superuser
        )


# ==================== AUTHENTICATION VIEWS ====================

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Naila Salsabila",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)

        response = redirect("main:show_main")
        response.set_cookie(
            "last_login",
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        return response

    context = {
        "name": "Naila Salsabila",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)

    response = redirect("main:login")
    response.delete_cookie("last_login")
    return response


# ==================== MAIN PROFILE VIEW ====================

def show_main(request):
    last_login = request.COOKIES.get(
        "last_login",
        "Belum ada sesi login / Cookie tidak ditemukan",
    )

    context = {
        "name": "Naila Salsabila",
        "npm": "2506620702",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "S1 Information System student at Fasilkom UI. Passionate about "
            "modern web development, system analysis, and technology innovation."
        ),
        "last_login": last_login,
    }

    return render(request, "index.html", context)


# ==================== PROJECT VIEWS ====================

def show_project(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Naila Salsabila",
        "title_query": title_query,
        "is_editor": is_editor(request.user),
        "form": ProjectForm(),
    }

    return render(request, "projects.html", context)


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related("starred_by").all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = []

    for project in projects:
        starred_users = project.starred_by.all()

        is_starred = (
            project.starred_by.filter(pk=request.user.pk).exists()
            if request.user.is_authenticated
            else False
        )

        starred_by_names = ", ".join(
            [user.username for user in starred_users]
        )

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "link_url": project.link_url or "",
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            },
        })

    return JsonResponse(data, safe=False)


@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)

    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {
                "message": "Proyek berhasil ditambahkan.",
                "pk": str(project.id),
            },
            status=201,
        )

    return JsonResponse(
        {"errors": form.errors.get_json_data()},
        status=400,
    )


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None, instance=None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_project")

    context = {
        "name": "Naila Salsabila",
        "form": form,
    }

    return render(request, "projects_form.html", context)


@login_required(login_url="/login/")
def edit_project(request, id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_project")

    context = {
        "name": "Naila Salsabila",
        "form": form,
    }

    return render(request, "projects_form.html", context)


@login_required(login_url="/login/")
def delete_project(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=id)

    if request.method == "POST":
        project.delete()

    return redirect("main:show_project")


def show_json(request):
    data = Project.objects.all()
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json",
    )


# ==================== EXPERIENCE VIEWS ====================

def show_experience(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Naila Salsabila",
        "title_query": title_query,
        "is_editor": is_editor(request.user),
        "form": ExperienceForm(),
    }

    return render(request, "experience.html", context)


def show_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []

    for exp in experiences:
        data.append({
            "pk": str(exp.id),
            "fields": {
                "title": exp.title,
                "description": exp.description,
                "category": exp.get_category_display(),
                "started_at": (
                    exp.started_at.strftime("%Y-%m-%d")
                    if exp.started_at else ""
                ),
                "ended_at": (
                    exp.ended_at.strftime("%Y-%m-%d")
                    if exp.ended_at else ""
                ),
            },
        })

    return JsonResponse(data, safe=False)


@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pengalaman."},
            status=403,
        )

    form = ExperienceForm(request.POST)

    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {
                "message": "Pengalaman berhasil ditambahkan.",
                "pk": str(experience.id),
            },
            status=201,
        )

    return JsonResponse(
        {"errors": form.errors.get_json_data()},
        status=400,
    )


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")

    context = {
        "name": "Naila Salsabila",
        "form": form,
    }

    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def edit_experience(request, id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")

    context = {
        "name": "Naila Salsabila",
        "form": form,
    }

    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def delete_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=id)

    if request.method == "POST":
        experience.delete()

    return redirect("main:show_experience")


# ==================== STAR FEATURE VIEW ====================

@login_required(login_url="/login/")
@require_POST
def toggle_star(request, id):
    project = get_object_or_404(Project, pk=id)

    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)

    return redirect("main:show_project")


# ==================== REST API VIEWS (DRF) ====================

# EXPERIENCE API

@api_view(["GET", "POST"])
@permission_classes([IsSuperuserOrReadOnly])
def experience_list_create_api(request):
    if request.method == "GET":
        experiences = Experience.objects.prefetch_related("starred_by").all()

        title = request.query_params.get("title", "").strip()
        if title:
            experiences = experiences.filter(title__icontains=title)

        serializer = ExperienceSerializer(
            experiences,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    serializer = ExperienceSerializer(
        data=request.data,
        context={"request": request},
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsSuperuserOrReadOnly])
def experience_detail_api(request, id):
    experience = get_object_or_404(
        Experience.objects.prefetch_related("starred_by"),
        pk=id,
    )

    if request.method == "GET":
        serializer = ExperienceSerializer(
            experience,
            context={"request": request},
        )
        return Response(serializer.data)

    if request.method in ["PUT", "PATCH"]:
        serializer = ExperienceSerializer(
            experience,
            data=request.data,
            partial=request.method == "PATCH",
            context={"request": request},
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    experience.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# PROJECT API

@api_view(["GET", "POST"])
@permission_classes([IsSuperuserOrReadOnly])
def project_list_create_api(request):
    if request.method == "GET":
        projects = Project.objects.prefetch_related("starred_by").all()

        title = request.query_params.get("title", "").strip()
        if title:
            projects = projects.filter(title__icontains=title)

        serializer = ProjectSerializer(
            projects,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    serializer = ProjectSerializer(
        data=request.data,
        context={"request": request},
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsSuperuserOrReadOnly])
def project_detail_api(request, id):
    project = get_object_or_404(
        Project.objects.prefetch_related("starred_by"),
        pk=id,
    )

    if request.method == "GET":
        serializer = ProjectSerializer(
            project,
            context={"request": request},
        )
        return Response(serializer.data)

    if request.method in ["PUT", "PATCH"]:
        serializer = ProjectSerializer(
            project,
            data=request.data,
            partial=request.method == "PATCH",
            context={"request": request},
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
