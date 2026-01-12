from django.urls import path
from .views import EntranceView

app_name = "entrance"

urlpatterns = [
	path('', EntranceView.as_view(), name='entrance'),
]