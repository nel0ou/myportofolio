from django import forms
from main.models import Project

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