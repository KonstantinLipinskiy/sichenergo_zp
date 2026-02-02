# from django.test import TestCase
# from service.models import ServiceInform
# from django.urls import reverse
# from news.models import NewsItem

# class ServiceInformTest(TestCase):
# 	def setUp(self):
# 		ServiceInform.objects.create(
# 			title="Заголовок Тест",
# 			name="Назва події Тест",
# 			video="video",
# 			description="Опис Тест"
# 		)
# 		NewsItem.objects.create(
# 			title="Тест",
# 			content="Текст",
# 			content_type="image",
# 			content_file = "test.jpg",
# 			region="Київ",
# 			heading="Ремонт"
# 		)
	
	
# 	def test_service_get(self):
# 		url = reverse("service:service")
# 		response = self.client.get(url)
# 		self.assertEqual(response.status_code, 200)
# 		self.assertTemplateUsed(response, "service/service.html")
# 		self.assertIn("serviceinform", response.context)
# 		self.assertIn("news", response.context)
# 		self.assertEqual(response.context["title"], "Послуги")