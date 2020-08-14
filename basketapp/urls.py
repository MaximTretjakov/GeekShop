from django.urls import path
from basketapp.views import BasketAddPageView, BasketHomePageView, BasketRemovePageView, BasketEditPageView

app_name = 'basketapp'

urlpatterns = [
    path('', BasketHomePageView.as_view(), name='view'),
    path('add/<int:pk>/', BasketAddPageView.as_view(), name='add'),
    path('remove/<int:pk>/', BasketRemovePageView.as_view(), name='remove'),
    path('edit/<int:pk>/<int:quantity>/', BasketEditPageView.as_view(), name='edit'),
]
