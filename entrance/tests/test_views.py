from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class EntranceViewTest(TestCase):
	def setUp(self):
		User.objects.create_user(username='admin', password='adminpass')

	def test_entrance_get(self):
		url = reverse("entrance:entrance")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'entrance/entrance.html')
		self.assertIn(response.context['title'], 'Вхід')
	
	def test_entrance_valid(self):
		url = reverse("entrance:entrance")
		response = self.client.post(url, {
			"username": "admin",
			"password": "adminpass"
		})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, '/admin/')

	def test_entrance_invalid(self):
		url = reverse("entrance:entrance")
		response = self.client.post(url, {
			"username": "wrong",
			"password": "wrong"
		})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, '/entrance/')
