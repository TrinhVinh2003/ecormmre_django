from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
  path("",views.index,name="index"),
  path("signup/",views.Signup,name="signup"),
  path("login/",views.LoginUser.as_view(),name ="login"),
  
]+ static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
