from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from shop.models import Category,Product

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','password1','password2','email']
from django import forms
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields ='__all__'

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','image','price','stock','category']

class AddStockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['stock']