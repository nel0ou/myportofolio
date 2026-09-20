from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm

def show_main(request):
    context = {
        "name": "Naila Salsabila",
        "npm": "2506620702",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "S1 Information System student at Fasilkom UI. Passionate about "
            "modern web development, system analysis, and technology innovation."
        ),
    }
    return render(request, "index.html", context)

def show_project(request):
    project_list = Project.objects.all()

    context = {
        "name": "Naila Salsabila",
        "project_list": project_list,
    }
    return render(request, "projects.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_project")

    context = {"name": "Naila Salsabila", "form": form}
    return render(request, "projects_form.html", context)

def edit_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_project")

    context = {"name": "Naila Salsabila", "form": form}
    return render(request, "projects_form.html", context)

def delete_project(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == "POST":
        project.delete()
    return redirect("main:show_project")

def show_json(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_experience(request):
    context = {
        "name": "Naila Salsabila",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_experience")

    context = {"name": "Naila Salsabila", "form": form}
    return render(request, "experience_form.html", context)

def edit_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_experience")

    context = {"name": "Naila Salsabila", "form": form}
    return render(request, "experience_form.html", context)

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
    return redirect("main:show_experience")

def show_experience_json(request):
    data = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")