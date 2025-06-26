from django.shortcuts import render,redirect
from .models import Product
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# def Index(request):
#     return render(request, 'home/index.html')

def all(request):
    products=Product.objects.all()
    return render(request,'home/index.html',{'products':products})

@login_required
def Detail(request,id):
    product = Product.objects.get(id = id)
    return render(request, 'home/detail.html', {'product': product})

def GetAllProductByCategory(request,category_id):
    product = Product.objects.filter(category_id = category_id)
    print(product.count()) 
    return render(request, 'home/get_all_by_category.html', {'products': product})

def Register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html',{'form':form})

# def Login(request):
#     if request.method == 'Post':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration/register.html',{'form':form})
def Logout(request):
    logout(request)
    return redirect("/")