from django.urls import path
from .views import CompanyView, AboutView, DocumentsView, ReviewsView

app_name = "company"

urlpatterns = [
	path('', CompanyView.as_view(), name='company'),
	path('about/', AboutView.as_view(), name='about'),
	path('documents/', DocumentsView.as_view(), name='documents'),
	path('reviews/', ReviewsView.as_view(), name='reviews'),
]