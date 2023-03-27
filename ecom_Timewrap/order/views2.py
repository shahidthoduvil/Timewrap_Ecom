from django.shortcuts import render,redirect
from.models import Order,OrderItem
from product.models import Coupon
from django.contrib import messages


def orderlist(request):
    context = {
        'orders' : Order.objects.all(),
        'items' : OrderItem.objects.all()
    }
    
    return render(request,'admin/orderlist.html', context)


def coupon_list(request):
    context={
        'coupon':Coupon.objects.all()
    }

    return render(request,"admin/coupon.html",context)


def add_coupon(request):
    if request.method=='POST':
        coupon_name=request.POST.get('coupon_code')
        discount_price=request.POST.get('discount_price')
        min_amount=request.POST.get('min_amount')
        
        Coupon.objects.create(
            coupon_code=coupon_name,
            min_amount=min_amount, 
           discount_price=discount_price, 
        
            )
        messages.success(request,f'{coupon_name} created successfully')
        return redirect(coupon_list)
    else:
        return redirect(coupon_list)







def delete_coupon(request):
    if request.method=='POST':
        coupon_id=request.POST.get('coupon_id')
        
        try:
            coupon=Coupon.objects.get(id=coupon_id)
            coupon.delete()
            messages.success(request,f'deleted{coupon}successfully')
            return redirect(coupon_list)
        except: 
            messages.error(request, f'Invalid coupon ID: {coupon_id}')
            return redirect(coupon_list)
    else:
        messages.error(request,f'something went wrong')
        return redirect(coupon_list)
    
   


