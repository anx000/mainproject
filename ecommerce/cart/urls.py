"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from cart import views
app_name = 'cart'
urlpatterns = [
    path('addtocart/<int:i>',views.AddtoCart.as_view(),name='addtocart'),
    path('remove/<int:i>/', views.CartDecrement.as_view(), name='remove'),
    path('delete/<int:i>/', views.CartRemove.as_view(), name='delete'),
    path('cartview/',views.CartView.as_view(),name='cartview'),
    path('checkout/',views.CheckOut.as_view(),name="checkout"),
    path('success/<i>',views.PaymentSuccess.as_view(),name="success"),
    path('yourorder/',views.YourOrder.as_view(),name='yourorder'),
]
