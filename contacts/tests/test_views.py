from django.test import TestCase
from django.urls import reverse
from contacts.models import Contacts, ContactsLocation
from django.core.files.uploadedfile import SimpleUploadedFile

class ContactsViewTest(TestCase):
	def setUp(self):
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