from django.urls import path
from mainapp.views import HomePageView, ProductsPageView, ContactPageView

app_name = 'mainapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('products/', ProductsPageView.as_view(), name='products'),
    path('products/category/<int:pk>', ProductsPageView.as_view(), name='products_id'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
