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
    project_list = [
        {
            'title': 'AmanIn – Smart Campus Safety Platform',
            'description': 'Peran: Chief Marketing Officer (CMO). Platform keamanan kampus berbasis aplikasi mobile yang menyediakan fitur Quick Report, Crowdsourced Map, 24/7 HelpDesk, dan Friend Tracker untuk meningkatkan keselamatan mahasiswa di Universitas Indonesia.',
            'tech_stack': 'Strategy Deck, Marketing & Business Strategy, UI/UX Prototyping, Pitching',
            'link_url': 'https://drive.google.com/LINK_DRIVE_AMANIN'
        },
        {
            'title': 'Evaluasi SI & Infrastruktur TI – PT Arutmin Indonesia',
            'description': 'Peran: Anggota Tim Riset (FiveG Team). Analisis strategi tata kelola dan sistem informasi pertambangan, mengevaluasi integrasi ERP Ellipse dan AIMS, serta merancang usulan solusi Low-Code Platform untuk efisiensi operasional.',
            'tech_stack': 'IT Governance, Business Process Analysis, System Architecture, Enterprise Systems',
            'link_url': 'https://drive.google.com/LINK_DRIVE_ARUTMIN'
        },
        {
            'title': 'IT Decision-Making Study – PT Gastera Prima Energi',
            'description': 'Peran: Anggota Tim Riset (Kelompok B01). Studi kasus dan wawancara mendalam mengenai proses pengambilan keputusan adopsi teknologi monitoring distribusi gas secara real-time berbasis sensor.',
            'tech_stack': 'Qualitative Research, IT Management, Risk & Operations Analysis',
            'link_url': 'https://drive.google.com/LINK_DRIVE_GASTERA'
        },
    ]

    context = {
        "name": "Naila Salsabila",
        "project_list": project_list,
    }
    return render(request, "projects.html", context)