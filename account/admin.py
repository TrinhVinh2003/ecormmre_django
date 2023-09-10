from django.contrib import admin
from .models import InforAccount,Cart
# Register your models here.
@admin.register(InforAccount)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','company','locality','city','mobile']

@admin.register(Cart)
class  CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']