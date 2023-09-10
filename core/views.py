from django.shortcuts import render,HttpResponse,redirect

from item.models import Category,Item
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth import login as auth_login
from django.views import View
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    item =Item.objects.filter(is_sold=False)[0:8]
    categories = Category.objects.all()
    return render(request,"core/index.html",{
        'category':categories,
        'item':item,
    })


def Signup(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1  = request.POST.get('password1')
        pass2  = request.POST.get('password2')
        if(pass1!= pass2):
            messages.error(request,"Error")
        else:
            my_user =User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect("/")
    return render(request,'core/signup.html',locals())
class LoginUser(View):
    def get(self,request):
        return render(request, "core/login.html")
    def post(self,request):
        username  =request.POST['username']
        password  =request.POST['password']
        
         
        user  =authenticate(request,username = username,password=password)
  
        if user is not None:
            auth_login(request,user)
            messages.success(request,"COngratuation")
            return redirect("/")
        return HttpResponse("saimk")
