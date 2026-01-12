from django.shortcuts import render
from .models import ModelItem
from django.views import View

class ModelItemView(View):
	def get(self, request):
		items = ModelItem.objects.all()
		context = {
			'title': 'Головна',
			'items': items,
		}

		return render(request, 'main/index.html', context)

