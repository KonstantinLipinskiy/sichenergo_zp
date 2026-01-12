from django.contrib import admin
from .models import ModelItem

@admin.register(ModelItem)
class ModelItemAdmin(admin.ModelAdmin):
	list_display = ["title", "image", "detail_url"]