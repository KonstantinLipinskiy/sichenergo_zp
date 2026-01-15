from django.shortcuts import render
from .models import ServiceInform
from django.views import View
from news.models import NewsItem

class ServiceView(View):
	def get(self, request):
		serviceinform = ServiceInform.objects.all()
		news = NewsItem.objects.filter(heading='Ремонт').first()
		context = {
			"title": "Послуги",
			"serviceinform": serviceinform,
			"news": news,
		}

		return render(request, 'service/service.html', context)