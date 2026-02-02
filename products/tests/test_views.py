from django.test import TestCase
from products.models import InformKTP, InformTransform, TransformItem, TransformTm, TransformTmg, TransformTmz, TransformYZ
from django.urls import reverse
from news.models import NewsItem
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch


class ProductsViewTest(TestCase):
	def setUp(self):
		patcher1 = patch("cloudinary.uploader.upload_resource") 
		patcher2 = patch("cloudinary.uploader.upload") 
		self.mock_upload_resource = patcher1.start() 
		self.mock_upload = patcher2.start() 
		self.mock_upload_resource.return_value = "fakefile"
		self.mock_upload.return_value = { 
			"public_id": "fakefile", 
			"version": "1234567890", 
			"format": "jpg", 
			"resource_type": "image", 
			"type": "upload", 
			"url": "http://example.com/fakefile.jpg", 
			"secure_url": "https://example.com/fakefile.jpg" 
			} 
		self.addCleanup(patcher1.stop) 
		self.addCleanup(patcher2.stop)

		TransformItem.objects.create(
			name="Трансформатор тест",
			image=SimpleUploadedFile('test.jpg', b'file_content', content_type='image/jpeg')
		)
		NewsItem.objects.create(
			title="Тест",
			content="Текст",
			content_type="image",
			content_file = "test.jpg",
			region="Київ",
			heading="Поставка"
		)

	def test_products_get(self):
		url = reverse('products:transformers')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "products/transformers.html")
		self.assertIn("series", response.context)
		self.assertIn("news", response.context)
		self.assertEqual(response.context["title"], "Трансформатори")

class TransformersTmViewTest(TestCase):
	def setUp(self):
		patcher1 = patch("cloudinary.uploader.upload_resource") 
		patcher2 = patch("cloudinary.uploader.upload") 
		self.mock_upload_resource = patcher1.start() 
		self.mock_upload = patcher2.start() 
		self.mock_upload_resource.return_value = "fakefile"
		self.mock_upload.return_value = { 
			"public_id": "fakefile", 
			"version": "1234567890", 
			"format": "jpg", 
			"resource_type": "image", 
			"type": "upload", 
			"url": "http://example.com/fakefile.jpg", 
			"secure_url": "https://example.com/fakefile.jpg" 
			} 
		self.addCleanup(patcher1.stop) 
		self.addCleanup(patcher2.stop)

		TransformTm.objects.create(
			name="Трансформатор ТМ Тест",
			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
			file_tm=SimpleUploadedFile("test.pdf", b"pdf_content", content_type="application/pdf")
		)
		InformTransform.objects.create(
			title="Скачати ОЛ Тест",
			description="Опис Тест",
			video="video",
			file_ol=SimpleUploadedFile("test.jpg", b"pdf_content", content_type="application/pdf")
		)

	def test_transformers_tm(self):
		url = reverse("products:tm")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "products/tm.html")
		self.assertIn("trans_tm", response.context)
		self.assertIn("inform", response.context)
		self.assertEqual(response.context["title"], "ТМ та ТМЖ")

class TransformTmgViewTest(TestCase):
	def setUp(self):
		patcher1 = patch("cloudinary.uploader.upload_resource") 
		patcher2 = patch("cloudinary.uploader.upload") 
		self.mock_upload_resource = patcher1.start() 
		self.mock_upload = patcher2.start() 
		self.mock_upload_resource.return_value = "fakefile"
		self.mock_upload.return_value = { 
			"public_id": "fakefile", 
			"version": "1234567890", 
			"format": "jpg", 
			"resource_type": "image", 
			"type": "upload", 
			"url": "http://example.com/fakefile.jpg", 
			"secure_url": "https://example.com/fakefile.jpg" 
			} 
		self.addCleanup(patcher1.stop) 
		self.addCleanup(patcher2.stop)

		TransformTmg.objects.create(
			name="Трансформатор ТМГ Тест",
			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
			file_tmg=SimpleUploadedFile("test.pdf", b"pdf_content", content_type="application/pdf")
		)
		InformTransform.objects.create(
			title="Скачати ОЛ Тест",
			description="Опис Тест",
			video="video",
			file_ol=SimpleUploadedFile("test.pdf", b"pdf_content", content_type="application/pdf")
		)
	
	def test_transform_tmg(self):
		url = reverse("products:tmg")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "products/tmg.html")
		self.assertIn("trans_tmg", response.context)
		self.assertIn("inform", response.context)
		self.assertEqual(response.context["title"], "ТМГ та ТМЖГ")

class TransformTmzViewTest(TestCase):
	def setUp(self):
		patcher1 = patch("cloudinary.uploader.upload_resource") 
		patcher2 = patch("cloudinary.uploader.upload") 
		self.mock_upload_resource = patcher1.start() 
		self.mock_upload = patcher2.start() 
		self.mock_upload_resource.return_value = "fakefile"
		self.mock_upload.return_value = { 
			"public_id": "fakefile", 
			"version": "1234567890", 
			"format": "jpg", 
			"resource_type": "image", 
			"type": "upload", 
			"url": "http://example.com/fakefile.jpg", 
			"secure_url": "https://example.com/fakefile.jpg" 
			} 
		self.addCleanup(patcher1.stop) 
		self.addCleanup(patcher2.stop)

		TransformTmz.objects.create(
			name="Трансформатор ТМЗ Тест",
			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
			file_tmz=SimpleUploadedFile("test.pdf", b"pdf_content", content_type="application/pdf")
		)
		InformTransform.objects.create(
			title="Скачати ОЛ Тест",
			description="Опис Тест",
			video="video",
			file_ol=SimpleUploadedFile("test.pdf", b"pdf_content", content_type="application/pdf")
		)

	def test_transform_tmz(self):
		url = reverse("products:tmz")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "products/tmz.html")
		self.assertIn("trans_tmz", response.context)
		self.assertIn("inform", response.context)
		self.assertEqual(response.context["title"], "ТМЗ")

class TransformersYzViewTest(TestCase):
	def setUp(self):
		patcher1 = patch("cloudinary.uploader.upload_resource") 
		patcher2 = patch("cloudinary.uploader.upload") 
		self.mock_upload_resource = patcher1.start() 
		self.mock_upload = patcher2.start() 
		self.mock_upload_resource.return_value = "fakefile"
		self.mock_upload.return_value = { 
			"public_id": "fakefile", 
			"version": "1234567890", 
			"format": "jpg", 
			"resource_type": "image", 
			"type": "upload", 
			"url": "http://example.com/fakefile.jpg", 
			"secure_url": "https://example.com/fakefile.jpg" 
			} 
		self.addCleanup(patcher1.stop) 
		self.addCleanup(patcher2.stop)

		TransformYZ.objects.create(
			name="Трансформатор YZ Тест",
			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
			file_yz=SimpleUploadedFile("test.pdf", b"pdf_content", content_type="application/pdf")
		)
		InformTransform.objects.create(
			title="Скачати ОЛ Тест",
			description="Опис Тест",
			video="video",
			file_ol=SimpleUploadedFile("test.pdf", b"pdf_content", content_type="application/pdf")
		)

	def test_transform_yz_get(self):
		url=reverse("products:yz")
		response=self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "products/tmg-yz.html")
		self.assertIn("trans_yz", response.context)
		self.assertIn("inform", response.context)
		self.assertEqual(response.context["title"], "Y/Z")

class KtpViewTest(TestCase):
	def setUp(self):
		patcher1 = patch("cloudinary.uploader.upload_resource") 
		patcher2 = patch("cloudinary.uploader.upload") 
		self.mock_upload_resource = patcher1.start() 
		self.mock_upload = patcher2.start() 
		self.mock_upload_resource.return_value = "fakefile"
		self.mock_upload.return_value = { 
			"public_id": "fakefile", 
			"version": "1234567890", 
			"format": "jpg", 
			"resource_type": "image", 
			"type": "upload", 
			"url": "http://example.com/fakefile.jpg", 
			"secure_url": "https://example.com/fakefile.jpg" 
			} 
		self.addCleanup(patcher1.stop) 
		self.addCleanup(patcher2.stop)

		InformKTP.objects.create(
			title="Ол Тест",
			description="Опис Тест",
			video="video",
			file_ol=SimpleUploadedFile("test.pdf", b"pdf_content", content_type="application/pdf")
		)

	def test_ktp_get(self):
		url = reverse("products:ktp")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "products/ktp.html")
		self.assertIn("ktp", response.context)
		self.assertEqual(response.context["title"], "КТП")