from django.urls import path
from .views import ModelItemView

app_name = 'main'

urlpatterns = [
	path('', ModelItemView.as_view(), name = 'index'),
]