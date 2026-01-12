from django.shortcuts import render, redirect
import logging
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages

logger = logging.getLogger(__name__)

class EntranceView(View):
	def get(self, request):
		context = {
			"title": "Вхід"
		}
		return render(request, 'entrance/entrance.html', context)

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			logger.info(f"User {username} successfull logged in.")
			messages.success(request, "Вхід виконано")
			return redirect('/admin/')
		else:
			logger.warning(f"Failed login attempt for username: {username}")
			messages.error(request, "Неправильне ім'я користувача або пароль")
			return redirect ('entrance:entrance')