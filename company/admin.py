from django.contrib import admin
from company.models import Presentation, DocumentsItem, ReviewsInfo, ReviewsItem

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
	list_display = ('title', 'image', 'description', 'file_present')

@admin.register(DocumentsItem)
class DocumentsItemAdmin(admin.ModelAdmin):
	list_display = ('title', 'image')

@admin.register(ReviewsInfo)
class ReviewsInfoAdmin(admin.ModelAdmin):
	list_display = ('title', 'image', 'name', 'description')

@admin.register(ReviewsItem)
class ReviewsIteAdmin(admin.ModelAdmin):
	list_display = ('title', 'image', 'description', 'name', 'region')