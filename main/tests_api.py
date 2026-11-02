from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from main.models import Experience, Project


class ExperienceAPITest(TestCase):
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

        self.experience = Experience.objects.create(
            title="Web Developer",
            description="Membuat website",
            category="internship",
        )

        self.list_url = "/api/experiences/"
        self.detail_url = f"/api/experiences/{self.experience.id}/"

    # 1. Semua pengguna dapat melihat daftar Experience
    def test_experience_list_public(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    # 2. Semua pengguna dapat melihat detail Experience
    def test_experience_detail_public(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Web Developer")

    # 3. Pencarian Experience dan hasil kosong
    def test_experience_search_and_empty(self):
        response = self.client.get(self.list_url, {"title": "Web"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.list_url, {"title": "TidakAda"})
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

        # Validasi menolak category yang tidak tersedia
        response = self.client.post(
            self.list_url,
            {
                "title": "Invalid",
                "description": "Data salah",
                "category": "kategori_salah",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    # 5. Superuser dapat melakukan PUT
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
        self.assertEqual(self.experience.title, "Backend Developer")

    # 6. Superuser dapat melakukan PATCH
    def test_superuser_patch_experience(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.patch(
            self.detail_url,
            {"title": "Frontend Developer"},
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Frontend Developer")

    # 7. Superuser dapat menghapus Experience
    def test_superuser_delete_experience(self):
        self.client.force_authenticate(user=self.superuser)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(
            Experience.objects.filter(pk=self.experience.pk).exists()
        )


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

        self.list_url = "/api/projects/"
        self.detail_url = f"/api/projects/{self.project.id}/"

    # 8. Semua pengguna dapat melihat daftar Project
    def test_project_list_public(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        # Pastikan password tidak muncul dalam respons
        self.assertNotIn("password", str(response.data))

    # 9. Semua pengguna dapat melihat detail Project
    def test_project_detail_public(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "RePair")

    # 10. Pencarian Project dan hasil kosong
    def test_project_search_and_empty(self):
        response = self.client.get(self.list_url, {"title": "RePair"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.list_url, {"title": "TidakAda"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    # 11. Pengguna biasa tidak dapat mengelola Project
    def test_regular_user_cannot_manage_project(self):
        self.client.force_authenticate(user=self.user)

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

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)

    # 12. Superuser dapat membuat, PUT, PATCH, dan DELETE Project
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

    # 13. Field Star tidak dapat diubah melalui API
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


class ProjectCSRFApiTest(TestCase):
    # Pengguna yang login dengan session harus menyertakan CSRF token
    def test_authenticated_write_without_csrf_is_rejected(self):
        user = User.objects.create_superuser(
            username="csrfadmin",
            email="csrf@example.com",
            password="password123",
        )

        client = APIClient(enforce_csrf_checks=True)
        client.login(username="csrfadmin", password="password123")

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