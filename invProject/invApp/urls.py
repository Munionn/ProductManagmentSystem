from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('create/', views.create_product, name="create_product"),
    path('list/', views.product_list_view, name="product_list"),
    path('delete/<int:product_id>/', views.delelte_view, name="product_delete"),
    path('update/<int:product_id>/', views.update_view, name='update_view'),

]