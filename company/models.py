from django.db import models

class Presentation(models.Model):
	title = models.CharField(max_length=155, verbose_name="Презентація")
	image = models.ImageField(upload_to='presentations/', default='deps/img/trans.png', verbose_name='Зображення')
	description = models.CharField(max_length=255, verbose_name="Опис")
	file_present = models.FileField(upload_to='presentations/files/', verbose_name="Файл для скачування")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Презентацію"
		verbose_name_plural = "Презентація"

class DocumentsInform(models.Model):
	title = models.CharField(max_length=155, verbose_name="Останні події")
	image = models.ImageField(upload_to='company/',verbose_name="Зображення")
	name = models.CharField(max_length=155, verbose_name="Короткий опис")
	description = models.TextField(verbose_name="Опис")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Подію"
		verbose_name_plural = "Документи події"

class DocumentsItem(models.Model):
	title = models.CharField(max_length=155, verbose_name="Найменування")
	image = models.ImageField(upload_to='company/', verbose_name="Зображення")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Документ"
		verbose_name_plural = "Документи"

class ReviewsInfo(models.Model):
	title = models.CharField(max_length=155, verbose_name="Додатковий сервіс")
	image = models.ImageField(upload_to='company/', verbose_name="Зображення")
	name = models.CharField(max_length=155, verbose_name="Короткий опис")
	description = models.TextField(verbose_name="Опис")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Сервіс"
		verbose_name_plural = "Відгуки Сервіс"

class ReviewsItem(models.Model):
	title = models.CharField(max_length=155, verbose_name="Назва компанії")
	image = models.ImageField(upload_to='company/', verbose_name="Зображення")
	description = models.TextField(verbose_name="Опис")
	name = models.CharField(max_length=155, verbose_name="Трансформатор")
	region = models.CharField(max_length=155, verbose_name="Регіон")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Відгук"
		verbose_name_plural = "Відгуки"
		ordering = ['-id']