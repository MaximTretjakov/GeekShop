from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from mainapp.views import HomePageView, ProductsPageView, ContactPageView, ProductPageView, products_ajax

app_name = 'mainapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('products/', ProductsPageView.as_view(), name='products'),
    path('product_page/<int:pk>', cache_page(3600)(ProductsPageView.as_view()), name='product_page'),
    path('products/category/<int:pk>', cache_page(3600)(ProductsPageView.as_view()), name='products_id'),
    path('products/category/<int:pk>/<int:page>/', ProductsPageView.as_view(), name='page'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    re_path(r'^products/category/(?P<pk>\d+)/ajax/$', cache_page(3600)(products_ajax)),
    re_path(r'^products/category/(?P<pk>\d+)/page/(?P<page>\d+)/ajax/$', cache_page(3600)(products_ajax)),
]
