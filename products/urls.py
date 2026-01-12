from django.urls import path
from .views import ProductsView, TransformersView, TransformersTmView, TransformersTmgView, TransformersTmzView, TransformersYzView, KtpView

app_name = "products"

urlpatterns = [
	path('', ProductsView.as_view(), name="products"),
	path('transformers/', TransformersView.as_view(), name="transformers"),
	path('transformers/tm/', TransformersTmView.as_view(), name="tm"),
	path('transformers/tmg/', TransformersTmgView.as_view(), name="tmg"),
	path('transformers/tmz/', TransformersTmzView.as_view(), name="tmz"),
	path('transformers/yz/', TransformersYzView.as_view(), name="yz"),
	path('ktp/', KtpView.as_view(), name="ktp"),
]