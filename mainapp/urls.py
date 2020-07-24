from django.urls import path
from mainapp.views import HomePageView, ProductsPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('products/', ProductsPageView.as_view(), name='products'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
