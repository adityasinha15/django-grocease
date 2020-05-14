"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from shop import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('reduce_cart/', views.reduce_cart, name='reduce_cart'),
    path('increase_cart/', views.increase_cart, name='increase_cart'),
    path('delete_session/', views.delete_session, name='delete_session'),
     path('delete_key/', views.delete_key, name='delete_key'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('show_quantity_cart/', views.show_quantity_cart, name='show_quantity_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove_product/', views.remove_product, name='remove_product'),
    path('empty_cart/', views.empty_cart, name='empty_cart'),
    #path('buy_now/<int:p_id>', views.buy_now, name='buy_now'),
    path('product_detail/<int:productId>', views.product_detail, name='product_detail'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
