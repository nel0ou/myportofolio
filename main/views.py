import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm

# HELPER: buat cek apakah user termasuk dalam grup Editor
def is_editor(user):
    return user.is_authenticated and user.groups.filter(name='Editor').exists()

# ==================== AUTHENTICATION VIEWS ====================

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")
    
    context = {"name": "Naila Salsabila", "form": form}
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        # Menambahkan cookie last_login saat berhasil login
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {"name": "Naila Salsabila", "form": form}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:login")
    # Menghapus cookie last_login saat logout
    response.delete_cookie('last_login')
    return response

# ==================== MAIN PROFILE VIEW ====================

def show_main(request):
    # Membaca cookie last_login dari request
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    
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
    project_list = Project.objects.all()
    context = {
        "name": "Naila Salsabila",
        "project_list": project_list,
        "is_editor": is_editor(request.user),
    }
    return render(request, "projects.html", context)

@login_required(login_url="/login/")
def create_project(request):
    # Server-side check: Hanya Superuser yang boleh Create
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_project")

    context = {"name": "Naila Salsabila", "form": form}
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def edit_project(request, id):
    # Server-side check: Superuser ATAU Editor yang boleh Edit
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_project")

    context = {"name": "Naila Salsabila", "form": form}
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def delete_project(request, id):
    # Server-side check: Hanya Superuser yang boleh Delete
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=id)
    if request.method == "POST":
        project.delete()
    return redirect("main:show_project")

def show_json(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# ==================== EXPERIENCE VIEWS ====================

def show_experience(request):
    context = {
        "name": "Naila Salsabila",
        "experience_list": Experience.objects.all(),
        "is_editor": is_editor(request.user),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    # Server-side check: Hanya Superuser yang boleh Create
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_experience")

    context = {"name": "Naila Salsabila", "form": form}
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def edit_experience(request, id):
    # Server-side check: Superuser ATAU Editor yang boleh Edit
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_experience")

    context = {"name": "Naila Salsabila", "form": form}
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, id):
    # Server-side check: Hanya Superuser yang boleh Delete
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
    return redirect("main:show_experience")

def show_experience_json(request):
    data = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# ==================== STAR FEATURE VIEW ====================

@login_required(login_url="/login/")
def toggle_star(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)
    return redirect("main:show_project")