
from django.urls import path, include
from . import views

urlpatterns = ([
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by-category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('price_search/', views.price_search, name='price_search'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    path('contact/', views.contact, name='contact'),
    path('update_product/<slug:product_slug>/', views.update_product, name='update_product'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<slug:product_slug>/', views.delete_product, name='delete_product'),
    path('my_store/<str:seller>/', views.my_store, name='my_store'),
    path('liveSearch/', views.liveSearch, name='liveSearch'),
    path('add_delete_variation/<int:pk>', views.prodVariation, name='prodVariation' ),
])

