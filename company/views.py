from django.shortcuts import render
from .models import DocumentsInform, DocumentsItem, Presentation, ReviewsInfo, ReviewsItem
from django.views import View
from news.models import NewsItem
from django.core.paginator import Paginator

class CompanyView(View):
	def get(self, request):
		return render(request)

class AboutView(View):
	def get(self, request):
		news = NewsItem.objects.filter(heading__in=['Компанія', 'Поза роботою', 'Виробництво']).order_by('-created_at').first()
		context = {
			"title": "Про нас",
			"news": news,
		}

		return render(request, 'company/about.html', context)

class DocumentsView(View):
	def get(self, request):
		items = DocumentsItem.objects.all()
		present = Presentation.objects.first()
		context = {
			"title": "Документи",
			"present": present,
			"items": items,
		}

		return render(request, 'company/documents.html', context)

class ReviewsView(View):
	def get(self, request):
		items = ReviewsItem.objects.all()
		paginator = Paginator(items, 9)
		page_number = request.GET.get("page")
		page_obj = paginator.get_page(page_number)
		inform = ReviewsInfo.objects.first()
		context = {
			"title": "Відгуки",
			"items": items,
			"page_obj": page_obj,
			"inform": inform,
		}

		return render(request, 'company/reviews.html', context)