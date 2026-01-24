from django.db import models
from cloudinary.models import CloudinaryField

class ModelItem(models.Model):
	title = models.CharField(max_length=255, verbose_name="Назва блоку")
	image = CloudinaryField(verbose_name="Зображення")
	detail_url = models.URLField(blank=True, null=True, verbose_name="Посилання")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Блок"
		verbose_name_plural = "Блок (перелік продукції та послуг)"