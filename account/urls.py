from django.urls import path
from . import views
from django.conf.urls.static import static

from django.contrib.auth import views as views_as
app_name = 'account'
urlpatterns = [
  path("",views.Account,name='useraccount'),
  path("address/",views.ProfileView.as_view(),name='address'),
  path("address/infor/",views.Info,name = 'infor'),
  path("updateAddress/<int:pk>",views.updateAddress.as_view(),name ='updateAddress'),
  path("delete/<int:pk>",views.deleteAddress,name = 'delete'),
  path("logout/",views.Logout,name = "logout"),
  path("cart/",views.show_cart,name = "cart"),
  path("add_to_cart",views.add_to_cart,name="add_to_cart"),
  path("pluscart/",views.plus_cart,name  ="pluscart"),
  path('minuscart/',views.minus_cart),
  path('removecart/',views.remove_cart),
  path("checkout/",views.checkout.as_view(),name="checkout")
]
