# from django.test import TestCase
# from company.models import DocumentsItem, Presentation, ReviewsInfo, ReviewsItem
# from django.urls import reverse
# from news.models import NewsItem
# from django.core.files.uploadedfile import SimpleUploadedFile


# class AboutViewTest(TestCase):
# 	def setUp(self):
# 		NewsItem.objects.create(
# 			title = "Тестова новина",
# 			content = "Текст",
# 			content_type= "image",
# 			content_file = "test.jpg",
# 			region = "Київ",
# 			heading= "Компанія"
# 		)

# 	def test_about_get(self):
# 		url = reverse('company:about')
# 		response = self.client.get(url)
# 		self.assertEqual(response.status_code, 200)
# 		self.assertTemplateUsed(response, 'company/about.html')
# 		self.assertIn("news", response.context)
# 		self.assertEqual(response.context['title'], 'Про нас')
# 		self.assertEqual(response.context['news'].title, 'Тестова новина')

# class DocumentsViewTest(TestCase):
# 	def sutUp(self):
# 		DocumentsItem.objects.create(
# 			title='Документ тест',
# 			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
# 		)
# 		Presentation.objects.create(
# 			title="Тест презентація",
# 			description="Тест опис презентація",
# 			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
# 			file_present=SimpleUploadedFile("test.pdf", b"pdf_content", content_type="application/pdf")
# 		)
	
# 	def test_documents_get(self):
# 		url = reverse("company:documents")
# 		response = self.client.get(url)
# 		self.assertEqual(response.status_code, 200)
# 		self.assertTemplateUsed(response, 'company/documents.html')
# 		self.assertIn("items", response.context)
# 		self.assertIn("present", response.context)
# 		self.assertEqual(response.context['title'], 'Документи')

# class ReviewsViewTest(TestCase):
# 	def setUp(self):
# 		ReviewsItem.objects.create(
# 			title='Назва компанії',
# 			description='Опис',
# 			name='Трансформатор',
# 			region='Київ',
# 			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
# 		)
# 		ReviewsInfo.objects.create(
# 			title='Додатковий сервіс',
# 			name='Короткий опис',
# 			description='Опис',
# 			image=SimpleUploadedFile("test.jpg", b"file_content", content_type='image/jpeg')
# 		)
	
# 	def test_reviews_get(self):
# 		url = reverse("company:reviews")
# 		response = self.client.get(url)
# 		self.assertEqual(response.status_code, 200)
# 		self.assertTemplateUsed(response, 'company/reviews.html')
# 		self.assertIn("items", response.context)
# 		self.assertIn("inform", response.context)
# 		self.assertEqual(response.context['title'], "Відгуки")