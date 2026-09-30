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
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Naila Salsabila",
        "title_query": title_query,
        "is_editor": is_editor(request.user),
        "form": ProjectForm(),  # Digunakan oleh Modal Tambah Proyek via AJAX
    }
    return render(request, "projects.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "link_url": getattr(project, 'link_url', ''),
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
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
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )
    
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@login_required(login_url="/login/")
def create_project(request):
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