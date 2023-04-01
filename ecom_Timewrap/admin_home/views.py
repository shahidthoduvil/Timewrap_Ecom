from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages,auth
from user.models import Account
from product.models import Product,Coupon,Category
from order.models import Order,OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from admin_product.views import superadmin_check
from django.urls import resolve



# Create your views here.
@user_passes_test(superadmin_check)
def admin_home(request):
  
    user = Account.objects.all().count()

    product = Product.objects.all().count()

    category = Category.objects.all().count()

    coupon = Coupon.objects.all().count()

    order = Order.objects.all().count()

    item = OrderItem.objects.all()
    
    context = {

        'user': user,
        'item': item,
        'category': category,
        'product': product,
        'coupon': coupon,
        'order': order,
    }
    return render(request,'admin_side/admin_home.html',context)


def admin_login(request):

    if request.method=='POST':
        email=request.POST['email']
        u_password=request.POST['password']

        print(email, u_password)

        user=authenticate(email=email,password=u_password)
        
        if user is not None:
            if user.is_superadmin:
                auth.login(request,user)
                return redirect(admin_home)
            else:
                messages.info(request,'you are not admin')
                return redirect(admin_login)
        else:
            messages.info(request,'invalid login credential')
            return redirect(admin_login)
    else:
        return render(request,"admin_side/admin_login.html") 
    

def admin_logout(request):
    auth.logout(request)
    return redirect(admin_login)



