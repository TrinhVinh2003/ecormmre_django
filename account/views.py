from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.views import View
from .forms import CustomerProfileForm
from .models import InforAccount,Cart
from item.models import Item
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
# Create your views here.
def Account(request):
    return render(request,"account/account.html")
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"account/address.html",locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name  = form.cleaned_data['name']
            company = form.cleaned_data['company']
            city  = form.cleaned_data['city']
            locals  = form.cleaned_data['locality']
            phone  = form.cleaned_data['mobile']
            reg =InforAccount(user= user,name =name,company = company,locality = locals,city= city,mobile=phone)
            reg.save()
            
            messages.success(request,"Congratulation ! Profile Save successfully")
        else:
            messages.warning(request,"Invalid Input Data")
       
        return redirect("infor/")

def Info(request):
    add = InforAccount.objects.filter(user =request.user)
    return render(request, "account/infor.html",{"adds":add})

class updateAddress(View):
    def get(self,request,pk):
        add = InforAccount.objects.get(pk=pk)
        form = CustomerProfileForm(instance= add)
        return render(request,"account/update.html",locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add  = InforAccount.objects.get(pk=pk)
            add.name  = form.cleaned_data["name"]
            add.company  = form.cleaned_data["company"]
            add.city  = form.cleaned_data["city"]
            add.locality  = form.cleaned_data["locality"]
            add.mobile  = form.cleaned_data["mobile"]
            add.save()
            messages.success(request,"Congratulations !")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect("account:infor")
def deleteAddress(request, pk):
    add  =InforAccount.objects.get(pk=pk)
    add.delete()

    return redirect("account:infor")
def Logout(request):
    logout(request)
    return redirect("/")

def add_to_cart(request):
    user = request.user
    product_id  = request.GET.get('prod_id')
    product = Item.objects.get(id =product_id)
    Cart(user=user,product=product).save()
    return redirect("cart/")

def show_cart(request):
    user = request.user
    cart  =Cart.objects.filter(user= user)
    amount  =0 
    for p in cart:
        value  =p.quantity *  p.product.price
        amount += value
        totalamount  =amount+   40

    return render(request,'account/cart.html',locals())

def plus_cart(request):
    if request.method =="GET":
        prod_id =request.GET['prod_id']
        c = Cart.objects.get(Q(product =prod_id)& Q(user =request.user))
        c.quantity +=1
        c.save()
        print(c.quantity)
        user = request.user
        cart  = Cart.objects.filter(user =user)
        amount  =0 
        for p in cart:
            value  =p.quantity *  p.product.price
            amount += value
            totalamount  =amount+   40
            print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
def minus_cart(request):
    if request.method =="GET":
        prod_id =request.GET['prod_id']
        c = Cart.objects.get(Q(product =prod_id)& Q(user =request.user))
        c.quantity -=1
        c.save()
        print(c.quantity)
        user = request.user
        cart  = Cart.objects.filter(user =user)
        amount  =0 
        for p in cart:
            value  =p.quantity *  p.product.price
            amount += value
            totalamount  =amount+   40
            print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
def remove_cart(request):
    if request.method =="GET":
        prod_id =request.GET['prod_id']
        c = Cart.objects.get(Q(product =prod_id)& Q(user =request.user))
        
        c.delete()
        print(c.quantity)
        user = request.user
        cart  = Cart.objects.filter(user =user)
        amount  =0 
        for p in cart:
            value  =p.quantity *  p.product.price
            amount += value
            totalamount  =amount+   40
            print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
class checkout(View):
    def get(self,request):
        user  = request.user
        add  =InforAccount.objects.filter(user=user)
        return render(request,"account/checkout.html",{"add":add})
    def post(self,request):
        pass