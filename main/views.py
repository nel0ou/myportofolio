from django.shortcuts import render
from main.models import Experience, Project

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

def show_experience(request):
    context = {
        "name": "Naila Salsabila",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_project(request):
    context = {
        "name": "Naila Salsabila",
        "project_list": Project.objects.all(),
    }
    return render(request, "projects.html", context)