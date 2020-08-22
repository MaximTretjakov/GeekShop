from django.urls import path
from mainapp.views import HomePageView, ProductsPageView, ContactPageView, ProductPageView

app_name = 'mainapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('products/', ProductsPageView.as_view(), name='products'),
    path('product_page/<int:pk>', ProductPageView.as_view(), name='product_page'),
    path('products/category/<int:pk>', ProductsPageView.as_view(), name='products_id'),
    path('products/category/<int:pk>/<int:page>/', ProductsPageView.as_view(), name='page'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
