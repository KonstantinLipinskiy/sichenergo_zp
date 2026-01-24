from django.db import models
from cloudinary.models import CloudinaryField

class ServiceInform(models.Model):
	title = models.CharField(max_length=155, blank=True, null=True, verbose_name="Заголовок")
	video = CloudinaryField(resource_type="video", blank=True, null=True, verbose_name="Відео")
	name = models.CharField(max_length=155, blank=True, null=True, verbose_name="Назва події")
	description = models.TextField(blank=True, null=True, verbose_name="Опис")

	def __str__(self):
		return self.name or self.title or "Без назви"

	class Meta:
		verbose_name = "Подію"
		verbose_name_plural = "Події"