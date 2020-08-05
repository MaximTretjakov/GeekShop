from django.urls import path
from django.contrib.auth.decorators import login_required
from mainapp.views import HomePageView, ProductsPageView, ContactPageView

app_name = 'mainapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('products/', login_required(ProductsPageView.as_view()), name='products'),
    path('products/<int:pk>', login_required(ProductsPageView.as_view()), name='products_id'),
    path('contact/', login_required(ContactPageView.as_view()), name='contact'),
]
