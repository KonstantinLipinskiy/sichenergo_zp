from django.shortcuts import render
from django.views import View
from .models import NewsItem

class NewsView(View):
	def get(self, request):
		news_items = NewsItem.objects.all()
		context = {
			"title": "Новини",
			"news_items": news_items,
		}

		return render(request, "news/news.html", context)