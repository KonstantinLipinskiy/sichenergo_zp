from django.contrib import admin
from .models import InformKTP, InformTransform, TransformItem, TransformTm, TransformTmg, TransformTmz, TransformYZ

@admin.register(TransformItem)
class TransformItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'image', 'detail_url')

@admin.register(InformTransform)
class InformTransformAdmin(admin.ModelAdmin):
	list_display = ('title', 'video', 'description', 'file_ol')

@admin.register(TransformTm)
class TransformTmAdmin(admin.ModelAdmin):
	list_display = ('name', 'image', 'file_tm')

@admin.register(TransformTmg)
class TransformTmgAdmin(admin.ModelAdmin):
	list_display = ('name', 'image', 'file_tmg')

@admin.register(TransformTmz)
class TransformTmzAdmin(admin.ModelAdmin):
	list_display = ('name', 'image', 'file_tmz')

@admin.register(TransformYZ)
class TransformYZAdmin(admin.ModelAdmin):
	list_display = ('name', 'image', 'file_yz')

@admin.register(InformKTP)
class InformKTPAdmin(admin.ModelAdmin):
	list_display = ('title', 'video', 'description', 'file_ol')