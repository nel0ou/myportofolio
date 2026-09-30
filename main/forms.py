from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", "category", "started_at", "ended_at"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Judul Pengalaman", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Deskripsi Pengalaman", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
            "category": forms.Select(attrs={"style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
            "started_at": forms.DateInput(attrs={"type": "date", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
            "ended_at": forms.DateInput(attrs={"type": "date", "style": "width: 100%; padding: 0.5rem; margin-top: 0.25rem;"}),
        }