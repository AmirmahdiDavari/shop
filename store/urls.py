from django.urls import path
from store.views import *

urlpatterns = [
    path("", index,name="index"),
    path("home", home,name="home"),
    path("cart/", cart_detile,name="cart_detile"),
    path("product/", product_page,name="product_page"),
]
