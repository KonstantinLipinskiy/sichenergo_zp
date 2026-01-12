from django.db import models

class ContactsLocation(models.Model):
	title = models.CharField(max_length=155, verbose_name="Геолокація")
	name = models.CharField(max_length=155, verbose_name="Короткий опис")
	map_url = models.URLField(verbose_name="Карта")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Локацію"
		verbose_name_plural = "Локація"

class Contacts(models.Model):
	telephone = models.CharField(max_length=155, verbose_name="Телефон")
	e_mail = models.CharField(max_length=155, verbose_name='e_mail')
	image = models.ImageField(upload_to='contacts/' ,verbose_name="Зображення")
	details = models.TextField(max_length=450, verbose_name="Реквізити")
	name = models.CharField(max_length=155, verbose_name="Контакти")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Контакт"
		verbose_name_plural = "Контакти"