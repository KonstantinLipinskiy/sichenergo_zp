from django.shortcuts import render
from .models import ModelItem
from django.views import View
from news.models import NewsItem

class ModelItemView(View):
	def get(self, request):
		items = ModelItem.objects.all()
		news = NewsItem.objects.order_by('-id').first()
		context = {
			'title': 'Головна',
			'items': items,
			'news': news,
		}

		return render(request, 'main/index.html', context)

