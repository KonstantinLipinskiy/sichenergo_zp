from django.shortcuts import render
from .models import DocumentsInform, DocumentsItem, Presentation, ReviewsInfo, ReviewsItem
from django.views import View

class CompanyView(View):
	def get(self, request):
		return render(request)

class AboutView(View):
	def get(self, request):
		present = Presentation.objects.all()
		context = {
			"title": "Про нас",
			"present": present,
		}

		return render(request, 'company/about.html', context)

class DocumentsView(View):
	def get(self, request):
		items = DocumentsItem.objects.all()
		inform = DocumentsInform.objects.all()
		context = {
			"title": "Документи",
			"inform": inform,
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