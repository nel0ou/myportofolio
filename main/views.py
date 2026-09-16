from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Experience, Project
from main.forms import ProjectForm

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
    # Data proyek bawaan kamu tetap disimpannn di sini
    default_projects = [
        {
            'title': 'AmanIn – Smart Campus Safety Platform',
            'description': 'Peran: Chief Marketing Officer (CMO). Platform keamanan kampus berbasis aplikasi mobile yang menyediakan fitur Quick Report, Crowdsourced Map, 24/7 HelpDesk, dan Friend Tracker untuk meningkatkan keselamatan mahasiswa di Universitas Indonesia.',
            'tech_stack': 'Strategy Deck, Marketing & Business Strategy, UI/UX Prototyping, Pitching',
            'link_url': 'https://drive.google.com/drive/folders/1U-vXLyRYeyj6rCIzUk0G83kuzEGBCAPa'
        },
        {
            'title': 'Evaluasi SI & Infrastruktur TI – PT Arutmin Indonesia',
            'description': 'Peran: Anggota Tim Riset (FiveG Team). Analisis strategi tata kelola dan sistem informasi pertambangan, mengevaluasi integrasi ERP Ellipse dan AIMS, serta merancang usulan solusi Low-Code Platform untuk efisiensi operasional.',
            'tech_stack': 'IT Governance, Business Process Analysis, System Architecture, Enterprise Systems',
            'link_url': 'https://drive.google.com/drive/folders/1A2AwgkImNWKNEnUFgR1J2Yw8cCL9B_Ou'
        },
        {
            'title': 'IT Decision-Making Study – PT Gastera Prima Energi',
            'description': 'Peran: Anggota Tim Riset (Kelompok B01). Studi kasus dan wawancara mendalam mengenai proses pengambilan keputusan adopsi teknologi monitoring distribusi gas secara real-time berbasis sensor.',
            'tech_stack': 'Qualitative Research, IT Management, Risk & Operations Analysis',
            'link_url': 'https://drive.google.com/drive/folders/1Rp7k9mNJO8VdLxNzI99Aqmldf7zFdWOO'
        },
    ]

    db_projects = Project.objects.all()

    # Jika DB kosong, pakai proyek bawaan. Jika DB ada isinya, pakai data DB.
    project_list = db_projects if db_projects.exists() else default_projects

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