from django.shortcuts import render
from django.views import View
from .models import NewsItem
from django.core.paginator import Paginator

class NewsView(View):
	def get(self, request):
		news_items = NewsItem.objects.all()
		paginator = Paginator(news_items, 2)
		page_number = request.GET.get("page")
		page_obj = paginator.get_page(page_number)
		context = {
			"title": "Новини",
			"news_items": news_items,
			"page_obj": page_obj,
		}

		return render(request, "news/news.html", context)