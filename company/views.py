from django.shortcuts import render
from .models import DocumentsInform, DocumentsItem, Presentation, ReviewsInfo, ReviewsItem
from django.views import View
from news.models import NewsItem

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
		inform = ReviewsInfo.objects.first()
		context = {
			"title": "Відгуки",
			"items": items,
			"inform": inform,
		}

		return render(request, 'company/reviews.html', context)