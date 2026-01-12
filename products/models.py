from django.db import models

class TransformItem(models.Model):
	name = models.CharField(max_length=150, verbose_name="Серія")
	image = models.ImageField(upload_to='transform/item/' ,verbose_name="Зображення")
	detail_url = models.URLField(blank=True, null=True, verbose_name="Посилання")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Серію"
		verbose_name_plural = "Серія трансформатора"

class InformTransform(models.Model):
	title = models.CharField(max_length=150, verbose_name="Трансформатор (опитовий лист)")
	video = models.FileField(upload_to='videos/', blank=True, null=True, verbose_name='Відео')
	description = models.TextField(verbose_name="Опис", blank=True)
	file_ol = models.FileField(upload_to='transform/ol/', verbose_name='Файл для скачування')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Опитувальний лист"
		verbose_name_plural = "Трансформатор - Опитувальні листи"

class TransformTm(models.Model):
	name = models.CharField(max_length=150, verbose_name="Потужність трансформаторів ТМ та ТМЖ")
	image = models.ImageField(upload_to='transform/tm/' ,verbose_name="Зображення")
	file_tm = models.FileField(upload_to='transform/file/tm/',verbose_name="Скачати креслення трансформаторів ТМ та ТМЖ")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Трансформатор ТМ та ТМЖ"
		verbose_name_plural = "Трансформатори ТМ та ТМЖ"

class TransformTmg(models.Model):
	name = models.CharField(max_length=150, verbose_name="Потужність трансформаторів ТМГ та ТМЖ")
	image = models.ImageField(upload_to='transform/tmg/' ,verbose_name="Зображення")
	file_tmg = models.FileField(upload_to='transform/file/tmg/',verbose_name="Скачати креслення трансформаторів ТМГ та ТМЖ")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Трансформатор ТМГ та ТМЖ"
		verbose_name_plural = "Трансформатори ТМГ та ТМЖ"

class TransformTmz(models.Model):
	name = models.CharField(max_length=150, verbose_name="Трансформатори ТМЗ")
	image = models.ImageField(upload_to='transform/tmz/',verbose_name="Зображення")
	file_tmz = models.FileField(upload_to='transform/file/tmz/',verbose_name="Скачати креслення трансформаторів ТМЗ")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Трансформатор ТМЗ"
		verbose_name_plural = "Трансформатори ТМЗ"

class TransformYZ(models.Model):
	name = models.CharField(max_length=150, verbose_name="Трансформатори серії Y/Z")
	image = models.ImageField(upload_to='transform/yz/',verbose_name="Зображення")
	file_yz = models.FileField(upload_to='transform/file/yz/',verbose_name="Скачати креслення трансформаторів Y/Z")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Трансформатор Y/Z"
		verbose_name_plural = "Трансформатори Y/Z"

class InformKTP(models.Model):
	title = models.CharField(max_length=150, verbose_name="КТП (опитовий лист)")
	video = models.FileField(upload_to="videos/", blank=True, null=True, verbose_name="Відео")
	description = models.TextField(verbose_name="Опис", blank=True)
	file_ol = models.FileField(upload_to='ktp/ol/',verbose_name="Файл для скачування")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Опитувальний лист"
		verbose_name_plural = "КТП - Опитувальні листи"