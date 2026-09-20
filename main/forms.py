from django import forms
from main.models import Project, Experience

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "tech_stack", "link_url"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Judul Proyek", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Deskripsi Proyek", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
            "tech_stack": forms.TextInput(attrs={"placeholder": "Contoh: Django, Python, HTML/CSS", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
            "link_url": forms.URLInput(attrs={"placeholder": "https://...", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", "category", "started_at", "ended_at"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Judul Pengalaman", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Deskripsi Pengalaman", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
            "category": forms.Select(attrs={"style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
            # PASTIKAN WIDGET "thumbnail" JUGA SUDAH DIHAPUS
            "started_at": forms.DateInput(attrs={"type": "date", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
            "ended_at": forms.DateInput(attrs={"type": "date", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
        }