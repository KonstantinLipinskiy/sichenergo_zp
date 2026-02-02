from django.test import TestCase
from django.urls import reverse
from contacts.models import Contacts, ContactsLocation
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch

class ContactsViewTest(TestCase):
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

		Contacts.objects.create(
			name='test',
			telephone='555-44-22-33',
			details='Реквізити',
			e_mail='test@mail.com',
			image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
		)
		ContactsLocation.objects.create(
			title='Локація',
			name='Фізичне місцезнаходження виробництва',
			map_url='https://maps.google.com/?q=Kyiv'
		)

	def test_contacts_get(self):
		url = reverse('contacts:contacts')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'contacts/contacts.html')
		self.assertIn("contact", response.context)
		self.assertIn("location", response.context)
		self.assertEqual(response.context["title"], "Контакти")