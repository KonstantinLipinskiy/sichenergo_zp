from django.test import TestCase
from main.models import ModelItem
from news.models import NewsItem
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class ModelItemTest(TestCase):
	def setUp(self):
		ModelItem.objects.create(
			title="Трансформатори",
			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
		)
		NewsItem.objects.create(
			title="Тест",
			content="Текст",
			content_type="image",
			content_file = "test.jpg",
			region="Київ",
			heading="Енергетика"
		)

	def test_main_status_code(self):
		url = reverse("main:index")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_main_templates(self):
		url = reverse("main:index")
		response = self.client.get(url)
		self.assertTemplateUsed(response, 'main/index.html')

	def test_main_context(self):
		url = reverse("main:index")
		response = self.client.get(url)
		self.assertIn("items", response.context)
		self.assertIn("news", response.context)
		self.assertEqual(response.context['title'], "Головна")