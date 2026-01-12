from django.shortcuts import render
from .models import ServiceInform
from django.views import View

class ServiceView(View):
	def get(self, request):
		serviceinform = ServiceInform.objects.all()
		context = {
			"title": "Послуги",
			"serviceinform": serviceinform,
		}

		return render(request, 'service/service.html', context)