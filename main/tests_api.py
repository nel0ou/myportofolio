from django.contrib.auth.models import User, Group
from django.test import TestCase
from rest_framework.test import APIClient

from main.models import Experience, Project


# =====================================================
# EXPERIENCE API TESTS - TUGAS 6
# =====================================================

class ExperienceAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Membuat superuser
        self.superuser = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword123",
        )

        # Membuat pengguna biasa
        self.user = User.objects.create_user(
            username="user",
            password="userpassword123",
        )

        # Membuat grup Editor
        self.editor_group = Group.objects.create(name="Editor")

        # Membuat pengguna Editor
        self.editor = User.objects.create_user(
            username="editor",
            password="editorpassword123",
        )
        self.editor.groups.add(self.editor_group)

        # Membuat data Experience
        self.experience = Experience.objects.create(
            title="Web Developer",
            description="Membuat website",
            category="internship",
        )

        # URL Experience API Tugas 6
        self.list_url = "/api/v1/experiences/"
        self.detail_url = (
            f"/api/v1/experiences/{self.experience.id}/"
        )
        self.star_url = (
            f"/api/v1/experiences/{self.experience.id}/star/"
        )

    # 1. Visitor dapat melihat daftar Experience
    def test_experience_list_public(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)

    # 2. Visitor dapat melihat detail Experience
    def test_experience_detail_public(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Web Developer")

    # 3. Pencarian Experience
    def test_experience_search_and_empty(self):
        response = self.client.get(
            self.list_url,
            {"title": "Web"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            self.list_url,
            {"title": "TidakAda"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    # 4. Superuser dapat membuat Experience
    def test_superuser_create_experience(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.post(
            self.list_url,
            {
                "title": "UI Designer",
                "description": "Mendesain aplikasi",
                "category": "internship",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(
            Experience.objects.filter(title="UI Designer").exists()
        )

    # 5. Visitor tidak dapat membuat Experience
    def test_visitor_cannot_create_experience(self):
        count_before = Experience.objects.count()

        response = self.client.post(
            self.list_url,
            {
                "title": "Experience Baru",
                "description": "Deskripsi",
                "category": "internship",
            },
            format="json",
        )

        count_after = Experience.objects.count()

        self.assertEqual(response.status_code, 403)
        self.assertEqual(count_after, count_before)

    # 6. Pengguna biasa tidak dapat membuat Experience
    def test_regular_user_cannot_create_experience(self):
        self.client.force_authenticate(user=self.user)
        count_before = Experience.objects.count()

        response = self.client.post(
            self.list_url,
            {
                "title": "Experience Baru",
                "description": "Deskripsi",
                "category": "internship",
            },
            format="json",
        )

        count_after = Experience.objects.count()

        self.assertEqual(response.status_code, 403)
        self.assertEqual(count_after, count_before)

    # 7. Editor tidak dapat membuat Experience
    def test_editor_cannot_create_experience(self):
        self.client.force_authenticate(user=self.editor)
        count_before = Experience.objects.count()

        response = self.client.post(
            self.list_url,
            {
                "title": "Experience Baru",
                "description": "Deskripsi",
                "category": "internship",
            },
            format="json",
        )

        count_after = Experience.objects.count()

        self.assertEqual(response.status_code, 403)
        self.assertEqual(count_after, count_before)

    # 8. Editor dapat mengedit Experience menggunakan PATCH
    def test_editor_can_patch_experience(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.patch(
            self.detail_url,
            {"title": "Frontend Developer"},
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        self.experience.refresh_from_db()
        self.assertEqual(
            self.experience.title,
            "Frontend Developer",
        )

    # 9. Editor tidak dapat menghapus Experience
    def test_editor_cannot_delete_experience(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 403)

        self.assertTrue(
            Experience.objects.filter(pk=self.experience.pk).exists()
        )

    # 10. Pengguna biasa tidak dapat mengedit Experience
    def test_regular_user_cannot_edit_experience(self):
        self.client.force_authenticate(user=self.user)
        original_title = self.experience.title

        response = self.client.patch(
            self.detail_url,
            {"title": "Judul Diubah"},
            format="json",
        )

        self.experience.refresh_from_db()

        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            self.experience.title,
            original_title,
        )

    # 11. Superuser dapat melakukan PUT
    def test_superuser_put_experience(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.put(
            self.detail_url,
            {
                "title": "Backend Developer",
                "description": "Mengembangkan backend",
                "category": "full-time",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        self.experience.refresh_from_db()
        self.assertEqual(
            self.experience.title,
            "Backend Developer",
        )

    # 12. Superuser dapat melakukan PATCH
    def test_superuser_patch_experience(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.patch(
            self.detail_url,
            {"title": "Frontend Developer"},
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        self.experience.refresh_from_db()
        self.assertEqual(
            self.experience.title,
            "Frontend Developer",
        )

    # 13. Superuser dapat menghapus Experience
    def test_superuser_delete_experience(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 204)

        self.assertFalse(
            Experience.objects.filter(pk=self.experience.pk).exists()
        )

    # 14. Serializer membersihkan input HTML
    def test_experience_serializer_validation(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.post(
            self.list_url,
            {
                "title": "<b>Data Analyst</b>",
                "description": "<p>Menganalisis data</p>",
                "category": "internship",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "Data Analyst")
        self.assertEqual(
            response.data["description"],
            "Menganalisis data",
        )

    # 15. Serializer menolak judul kosong setelah HTML dibersihkan
    def test_experience_rejects_empty_cleaned_title(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.post(
            self.list_url,
            {
                "title": "<b></b>",
                "description": "Deskripsi valid",
                "category": "internship",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Experience.objects.count(), 1)

    # 16. Pengguna login dapat memberikan dan membatalkan star
    def test_user_can_toggle_experience_star(self):
        self.client.force_authenticate(user=self.user)

        # Memberikan star
        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(
            self.experience.starred_by.count(),
            1,
        )

        # Membatalkan star
        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(
            self.experience.starred_by.count(),
            0,
        )

    # 17. Visitor tidak dapat memberikan star
    def test_visitor_cannot_star_experience(self):
        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            self.experience.starred_by.count(),
            0,
        )

    # 18. Field star tidak dapat diubah melalui input
    def test_experience_star_fields_are_read_only(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.post(
            self.list_url,
            {
                "title": "Project Star Test",
                "description": "Testing star",
                "category": "internship",
                "starred_by": [self.superuser.id],
                "star_count": 999,
                "is_starred": True,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)

        experience = Experience.objects.get(
            title="Project Star Test"
        )

        self.assertEqual(experience.starred_by.count(), 0)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])


# =====================================================
# EXPERIENCE API CSRF TEST
# =====================================================

class ExperienceCSRFApiTest(TestCase):

    def test_authenticated_write_without_csrf_is_rejected(self):
        User.objects.create_superuser(
            username="csrfadmin",
            email="csrf@example.com",
            password="password123",
        )

        client = APIClient(enforce_csrf_checks=True)

        client.login(
            username="csrfadmin",
            password="password123",
        )

        response = client.post(
            "/api/v1/experiences/",
            {
                "title": "Experience CSRF",
                "description": "Testing CSRF",
                "category": "internship",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 403)
        self.assertFalse(
            Experience.objects.filter(
                title="Experience CSRF"
            ).exists()
        )


# =====================================================
# PROJECT API TESTS - TUTORIAL 07
# =====================================================

class ProjectAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.superuser = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword123",
        )

        self.user = User.objects.create_user(
            username="user",
            password="userpassword123",
        )

        self.project = Project.objects.create(
            title="RePair",
            description="Aplikasi tukar barang",
            tech_stack="Django",
            link_url="https://example.com",
        )

        # URL Project Tutorial 07
        self.list_url = "/api/projects/"
        self.detail_url = f"/api/projects/{self.project.id}/"

    # 1. Semua pengguna dapat melihat daftar Project
    def test_project_list_public(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertNotIn("password", str(response.data))

    # 2. Semua pengguna dapat melihat detail Project
    def test_project_detail_public(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "RePair")

    # 3. Pencarian Project dan hasil kosong
    def test_project_search_and_empty(self):
        response = self.client.get(
            self.list_url,
            {"title": "RePair"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            self.list_url,
            {"title": "TidakAda"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    # 4. Pengguna biasa tidak dapat mengelola Project
    def test_regular_user_cannot_manage_project(self):
        self.client.force_authenticate(user=self.user)

        original_count = Project.objects.count()
        original_title = self.project.title

        response = self.client.post(
            self.list_url,
            {
                "title": "Project Baru",
                "description": "Deskripsi",
                "tech_stack": "Python",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Project.objects.count(), original_count)

        response = self.client.put(
            self.detail_url,
            {
                "title": "Diubah",
                "description": "Deskripsi baru",
                "tech_stack": "Python",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 403)

        response = self.client.patch(
            self.detail_url,
            {"title": "Diubah"},
            format="json",
        )

        self.assertEqual(response.status_code, 403)

        self.project.refresh_from_db()
        self.assertEqual(self.project.title, original_title)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Project.objects.filter(pk=self.project.pk).exists()
        )

    # 5. Superuser dapat membuat, PUT, PATCH, dan DELETE Project
    def test_superuser_project_crud(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.post(
            self.list_url,
            {
                "title": "Website Baru",
                "description": "Website portofolio",
                "tech_stack": "Django",
                "link_url": "https://example.com",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)

        new_project_id = response.data["id"]
        detail_url = f"/api/projects/{new_project_id}/"

        response = self.client.put(
            detail_url,
            {
                "title": "Website Diperbarui",
                "description": "Deskripsi baru",
                "tech_stack": "Python",
                "link_url": "https://example.com",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        response = self.client.patch(
            detail_url,
            {"title": "Website PATCH"},
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        response = self.client.delete(detail_url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(
            Project.objects.filter(pk=new_project_id).exists()
        )

    # 6. Field star tidak dapat diubah melalui API
    def test_project_star_fields_read_only(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.post(
            self.list_url,
            {
                "title": "Project Star",
                "description": "Testing Star",
                "tech_stack": "Django",
                "starred_by": [self.superuser.id],
                "star_count": 999,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)

        project = Project.objects.get(title="Project Star")

        self.assertEqual(project.starred_by.count(), 0)
        self.assertEqual(response.data["star_count"], 0)


# =====================================================
# PROJECT API CSRF TEST - TUTORIAL 07
# =====================================================

class ProjectCSRFApiTest(TestCase):

    def test_authenticated_write_without_csrf_is_rejected(self):
        User.objects.create_superuser(
            username="csrfadmin",
            email="csrf@example.com",
            password="password123",
        )

        client = APIClient(enforce_csrf_checks=True)

        client.login(
            username="csrfadmin",
            password="password123",
        )

        response = client.post(
            "/api/projects/",
            {
                "title": "Project CSRF",
                "description": "Testing CSRF",
                "tech_stack": "Django",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 403)
        self.assertFalse(
            Project.objects.filter(
                title="Project CSRF"
            ).exists()
        )