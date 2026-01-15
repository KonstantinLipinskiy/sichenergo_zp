from django.shortcuts import render
from .models import InformKTP, InformTransform, TransformItem, TransformTm, TransformTmg, TransformTmz, TransformYZ
from django.views import View
from news.views import NewsItem

class ProductsView(View):
	def get(self, request):
		return render(request)

class TransformersView(View):
	def get(self, request):
		series = TransformItem.objects.all()
		news = NewsItem.objects.filter(heading="Поставка").first()
		context = {
			"title": "Трансформатори",
			"series": series,
			"news": news,
		}

		return render(request, "products/transformers.html", context)

class TransformersTmView(View):
	def get(self, request):
		trans_tm = TransformTm.objects.all()
		inform = InformTransform.objects.first()
		context = {
			"title": "ТМ та ТМЖ",
			"trans_tm": trans_tm,
			"inform": inform,
		}

		return render(request, "products/tm.html", context)

class TransformersTmgView(View):
	def get(self, request):
		trans_tmg = TransformTmg.objects.all()
		inform = InformTransform.objects.first()
		context = {
			"title": "ТМГ та ТМЖГ",
			"trans_tmg": trans_tmg,
			"inform": inform,
		}

		return render(request, "products/tmg.html", context)

class TransformersTmzView(View):
	def get(self, request):
		trans_tmz = TransformTmz.objects.all()
		inform = InformTransform.objects.first()
		context = {
			"title": "ТМЗ",
			"trans_tmz": trans_tmz,
			"inform": inform,
		}

		return render(request, "products/tmz.html", context)

class TransformersYzView(View):
	def get(self, request):
		trans_yz = TransformYZ.objects.all()
		inform = InformTransform.objects.all()
		context = {
			"title": "Y/Z",
			"trans_yz": trans_yz,
			"inform": inform,
		}

		return render(request, "products/tmg-yz.html", context)

class KtpView(View):
	def get(self, request):
		ktp = InformKTP.objects.first()
		context = {
			"title": "КТП",
			"ktp": ktp,
		}

		return render(request, "products/ktp.html", context)