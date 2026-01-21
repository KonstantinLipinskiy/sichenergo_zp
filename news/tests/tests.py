from django.test import TestCase
from news.models import NewsItem
from django.urls import reverse

class NewsViewTest(TestCase):
	def setUp(self):
		NewsItem.objects.create(
			title = "Тестова новина",
			content = "Текст",
			content_type= "image",
			content_file = "test.jpg",
			region = "Київ",
			heading= "Енергетика"
		)

	def test_news_view_status_code(self):
		url = reverse("news:news")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_news_view_uses_templates(self):
		url = reverse("news:news")
		response = self.client.get(url)
		self.assertTemplateUsed(response, "news/news.html")

	def test_news_view_context(self):
		url = reverse("news:news")
		response = self.client.get(url)
		self.assertIn("news_items", response.content)
		self.assertEqual(response.content['title'], 'Новини')
		self.assertEqual(response.content['news_items'], 1)