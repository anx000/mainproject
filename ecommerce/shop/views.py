from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from shop.models import Category
from shop.models import Product
from django.contrib import messages
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
class AdminHomeView(View):
    def get(self,request):
        return render(request,'adminhome.html')

class CategoryViews(View):
    def get(self,request):
        c=Category.objects.all()
        context={'category':c}
        return render(request,'categories.html',context)


class ProductViews(View):
    def get(self, request,i):
        c = Category.objects.get(id=i)
        context = {'category': c}
        return render(request, 'products.html', context)

from shop.models import Product
class ProductDetailsViews(View):
      def get(self,request,i):
          p=Product.objects.get(id=i)
          context={'product':p}
          return render(request,'productdetails.html',context)
from shop.forms import SignupForm
class Register(View):
    def get(self,request):
        form_instance = SignupForm()
        return render(request,'register.html',{'form':form_instance})
    def post(self,request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:home')
        return render(request, 'register.html', {'form': form_instance})
from shop.forms import LoginForm
class Userlogin(View):
    def post(self,request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            name = form_instance.cleaned_data['username']
            pwd  = form_instance.cleaned_data['password']
            user = authenticate(username=name,password=pwd)
        if user and user.is_superuser == True:
            login(request, user)
            return redirect('shop:adminhome')
        elif user and user.is_superuser != True:
            login(request, user)
            return redirect('shop:home')
        else:
            messages.error(request,'invalid credentials')
            return render(request,'login.html',{'form',form_instance})
    def get(self,request):
        form_instance = LoginForm()
        return render(request, 'login.html', {'form': form_instance})

class Userlogout(View):
    def get(self,request):
        logout(request)
        return redirect('shop:login')
from shop.forms import AddCategoryForm
class AddCategory(View):
    def get(self,request):
        form_instance = AddCategoryForm()
        return render(request,'addcategory.html',{'form':form_instance})
    def post(self,request):
        form_instance = AddCategoryForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:adminhome')
        return render(request, 'addcategory.html', {'form': form_instance})

from shop.forms import AddProductForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
class AddProduct(LoginRequiredMixin,UserPassesTestMixin,View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self,request):
        form_instance = AddProductForm()
        return render(request,'addproduct.html',{'form':form_instance})
    def post(self,request):
        form_instance = AddProductForm(request.POST,request.FILES)
        if form_instance.is_valid:
            form_instance.save()
            return redirect('shop:adminhome')
        return render(request,'addproduct.html',{'form':form_instance})
from shop.forms import AddStockForm
class AddStock(View):
    def get(self,request,i):
        p=Product.objects.get(id=i)
        form_instance = AddStockForm(instance=p)
        return render(request,'addstock.html',{'form':form_instance})
    def post(self,request,i):
        p = Product.objects.get(id=i)
        form_instance = AddStockForm(request.POST,request.FILES,instance=p)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:adminhome')
        return render(request, 'addstock.html', {'form': form_instance})


class Search(View):
    def post(self,request):
        query = request.POST.get('q')
        products   = Product.objects.filter(Q(name__icontains=query))
        context = {'products':products}
        return render(request,'search.html',context)



