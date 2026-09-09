from django.shortcuts import render
from main.models import Experience

def show_main(request):
    context = {
        "name": "Naila Salsabila",
        "npm": "2506620702",
        "study_program": "S1 Sistem Informasi",
        "bio": "A Computer Science student at Universitas Indonesia interested in software development and education.",
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Naila Salsabila",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)