from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='eagle-home'),
    path('full_menu/', views.Product_list.as_view(), name='fashion-menu'),
    path('offer-products', views.offer_product, name='eagle-contact'),
    path('digital-content', views.digital_content, name='eagle-digitalcontent')
]