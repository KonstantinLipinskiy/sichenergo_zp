# from django.test import TestCase
# from news.models import NewsItem
# from django.urls import reverse

# class NewsViewTest(TestCase):
# 	def setUp(self):
# 		NewsItem.objects.create(
# 			title = "Тестова новина",
# 			content = "Текст",
# 			content_type= "image",
# 			content_file = "test.jpg",
# 			region = "Київ",
# 			heading= "Енергетика"
# 		)

# 	def test_news_get(self):
# 		url = reverse("news:news")
# 		response = self.client.get(url)
# 		self.assertEqual(response.status_code, 200)
# 		self.assertTemplateUsed(response, "news/news.html")
# 		self.assertIn("news_items", response.context)
# 		self.assertEqual(response.context['title'], 'Новини')
# 		self.assertEqual(len(response.context['news_items']), 1)