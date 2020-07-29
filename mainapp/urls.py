from django.urls import path

from mainapp.views import (
    HomePageView, ProductsPageView, ContactPageView,
    ProductsPageAllView, ProductsPageHomeView, ProductsPageOfficeView,
    ProductsPageModernView, ProductsPageClassicView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('products/', ProductsPageView.as_view(), name='products'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('products/all/', ProductsPageAllView.as_view(), name='products_all'),
    path('products/home/', ProductsPageHomeView.as_view(), name='products_house'),
    path('products/office/', ProductsPageOfficeView.as_view(), name='products_office'),
    path('products/modern/', ProductsPageModernView.as_view(), name='products_modern'),
    path('products/classic/', ProductsPageClassicView.as_view(), name='products_classic'),
]
