from django.contrib import admin
from .models import NewsItem

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
	list_display = ('title', 'region', 'heading', 'content_type', 'created_at')