from django.test import TestCase, Client
from main.models import Project

class ProjectTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_project_url_is_exist(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')

    def test_project_list_with_data(self):
        Project.objects.create(
            title="Portfolio Website",
            description="Web portofolio menggunakan Django",
            tech_stack="Django, HTML, CSS"
        )
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Portfolio Website")

    def test_project_list_empty(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada proyek yang ditampilkan.")