from django.urls import path
from adminapp.views import (
    UserCreatePageView, UsersListView, UserUpdatePageView, UserDeletePageView,
    CategoryCreatePageView, CategoriesPageView, CategoryUpdatePageView, CategoryDeletePageView,
    ProductCreatePageView, ProductsPageView, ProductUpdatePageView, ProductDeletePageView, ProductReadPageView
)

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', UserCreatePageView.as_view(), name='user_create'),
    # path('users/read/', UsersPageView.as_view(), name='users'),
    path('users/read/', UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', UserUpdatePageView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeletePageView.as_view(), name='user_delete'),

    path('categories/create/', CategoryCreatePageView.as_view(), name='category_create'),
    path('categories/read/', CategoriesPageView.as_view(), name='categories'),
    path('categories/update/<int:pk>/', CategoryUpdatePageView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', CategoryDeletePageView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>/', ProductCreatePageView.as_view(), name='product_create'),
    path('products/read/category/<int:pk>/', ProductsPageView.as_view(), name='products'),
    path('products/read/<int:pk>/', ProductReadPageView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', ProductUpdatePageView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeletePageView.as_view(), name='product_delete'),
]
