from django.test import TestCase
from company.models import DocumentsItem, Presentation, ReviewsInfo, ReviewsItem
from django.urls import reverse
from news.models import NewsItem
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch

class CloudinaryMockedTest(TestCase): 
	@classmethod 
	def setUpClass(cls): 
		super().setUpClass() 
		cls.patcher_upload_resource = patch("cloudinary.uploader.upload_resource") 
		cls.patcher_upload = patch("cloudinary.uploader.upload") 
		cls.mock_upload_resource = cls.patcher_upload_resource.start() 
		cls.mock_upload = cls.patcher_upload.start() 
		cls.mock_upload_resource.return_value = "fakefile" 
		cls.mock_upload.return_value = { 
			"public_id": "fakefile", 
			"version": "1234567890", 
			"format": "jpg", 
			"resource_type": "image", 
			"type": "upload", 
			"url": "http://example.com/fakefile.jpg", 
			"secure_url": "https://example.com/fakefile.jpg" 
			} 
			
		@classmethod 
		def tearDownClass(cls): 
			cls.patcher_upload_resource.stop() 
			cls.patcher_upload.stop() 
			super().tearDownClass()


class AboutViewTest(CloudinaryMockedTest):
	def setUp(self):
		NewsItem.objects.create(
			title = "Тестова новина",
			content = "Текст",
			content_type= "image",
			content_file = "test.jpg",
			region = "Київ",
			heading= "Компанія"
		)

	def test_about_get(self):
		url = reverse('company:about')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'company/about.html')
		self.assertIn("news", response.context)
		self.assertEqual(response.context['title'], 'Про нас')
		self.assertEqual(response.context['news'].title, 'Тестова новина')

class DocumentsViewTest(CloudinaryMockedTest):
	def sutUp(self):
		DocumentsItem.objects.create(
			title='Документ тест',
			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
		)
		Presentation.objects.create(
			title="Тест презентація",
			description="Тест опис презентація",
			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
			file_present=SimpleUploadedFile("test.pdf", b"pdf_content", content_type="application/pdf")
		)
	
	def test_documents_get(self):
		url = reverse("company:documents")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'company/documents.html')
		self.assertIn("items", response.context)
		self.assertIn("present", response.context)
		self.assertEqual(response.context['title'], 'Документи')

class ReviewsViewTest(CloudinaryMockedTest):
	def setUp(self):
		ReviewsItem.objects.create(
			title='Назва компанії',
			description='Опис',
			name='Трансформатор',
			region='Київ',
			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
		)
		ReviewsInfo.objects.create(
			title='Додатковий сервіс',
			name='Короткий опис',
			description='Опис',
			image=SimpleUploadedFile("test.jpg", b"file_content", content_type='image/jpeg')
		)
	
	def test_reviews_get(self):
		url = reverse("company:reviews")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'company/reviews.html')
		self.assertIn("items", response.context)
		self.assertIn("inform", response.context)
		self.assertEqual(response.context['title'], "Відгуки")