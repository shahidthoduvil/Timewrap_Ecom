from django.shortcuts import render, redirect
from product.models import Banner, Category, Product, Brand, Material,MultipleImg,Color,Variation,Coupon
from order.models import Order,OrderItem
from user.models import Account
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.


def list_product(request):

    product_dict = {
        'pro': Product.objects.all(),
        'cat': Category.objects.all(),
        'band': Brand.objects.all(),
        'material': Material.objects.all(),
        'colr': Color.objects.all()


    }
    return render(request, 'admin_side/list_product.html', product_dict)


def product_edit(request, id):
    if request.method == 'POST':
        pro_name = request.POST['product_name']
        pro_color = request.POST['product_color']
        slug = request.POST['slug']
        pro_category = request.POST['product_category']
        pro_brand = request.POST['product_brand']
        pro_material = request.POST['product_material']
        pro_description = request.POST['product_description']
        pro_specification = request.POST['product_specification']
        pro_price = request.POST['product_price']
        pro_stock = request.POST['product_stock']

        category_instance = Category.objects.get(id=pro_category)
        color_instance = Color.objects.get(id=pro_color)
        brand_instance = Brand.objects.get(id=pro_brand)
        material_instance = Material.objects.get(id=pro_material)

        update_product = Product.objects.get(id=id)

        pro_image = request.FILES['product_image']
        update_product.image = pro_image
        update_product.save()

        update_product = Product.objects.filter(id=id)

        update_product.update(title=pro_name, slug=slug, color=color_instance, description=pro_description, price=pro_price,
                              stock=pro_stock, category=category_instance, brand=brand_instance, material=material_instance,
                              specification=pro_specification)
        return redirect(list_product)

    return render(request, "admin_side/list_product.html")


def add_product(request):
    product_dict = {

        'cat': Category.objects.all(),
        'band': Brand.objects.all(),
        'material': Material.objects.all(),
        # 'colr': Color.objects.all()


    }

    if request.method == 'POST':
        pro_name = request.POST['name']
        slug = request.POST['slug']

        pro_description = request.POST['description']

        pro_specification = request.POST['specification']
        pro_price = request.POST['price']
        pro_stock = request.POST['stock']

        try:
            # pro_color = request.POST['color']
            pro_image = request.FILES['image']
            pro_category = request.POST['category']
            pro_material = request.POST['material']
            pro_brand = request.POST['brand']
        except MultiValueDictKeyError:

            pro_image = False
            pro_color = False
            pro_category = False
            pro_brand = False
            pro_material = False

        category_instance = Category.objects.get(id=pro_category)
        # color_instance = Color.objects.get(id=pro_color)
        brand_instance = Brand.objects.get(id=pro_brand)
        material_instance = Material.objects.get(id=pro_material)

        product = Product.objects.create(
            title=pro_name, slug=slug, description=pro_description, price=pro_price, stock=pro_stock, image=pro_image, category=category_instance, brand=brand_instance, material=material_instance, specification=pro_specification)
       
        multi_images = request.FILES.getlist('images')


        for image in multi_images:
            MultipleImg.objects.create(product=product,img=image)


       # product.save()
        return redirect(list_product)

    return render(request, 'admin_side/add_product.html', product_dict)


def product_delete(request, id):
    del_pro = Product.objects.filter(id=id)
    del_pro.delete()

    return redirect(list_product)


def material(request):
    mater_edit = {

        'material': Material.objects.all(),
    }
    return render(request, "admin_side/material.html", mater_edit)


# material edit


def material_edit(request, id):

    mat_name = request.POST['ma_name']
    slug = request.POST['slug']
    mat_update = Material.objects.filter(id=id)

    mat_update.update(material_name=mat_name, slug=slug)

    return redirect(material)

    # material add


def material_add(request):
    mat_name = request.POST['m_name']
    slug = request.POST['slug']

    mat_add = Material.objects.create(material_name=mat_name, slug=slug)
    mat_add.save()

    return redirect(material)

# material delete


def material_delete(request, id):
    del_mat = Material.objects.filter(id=id)
    del_mat.delete()
    return redirect(material)


def color(request):
    color_dict = {
        'colr': Color.objects.all()
    }

    return render(request, "admin_side/color.html", color_dict)


# color_edit


def color_edit(request, id):
    colr_name = request.POST['col_name']
    slug = request.POST['slug']
    color_update = Color.objects.filter(id=id)
    color_update.update(color_name=colr_name, slug=slug)
    return redirect(color)

# color_add


def color_add(request):
    c_name = request.POST['c_name']
    slug = request.POST['slug']
    color_add = Color.objects.create(color_name=c_name, slug=slug)
    color_add.save()
    return redirect(color)


# color_delete

def color_delete(request, id):
    colr_del = Color.objects.filter(id=id)
    colr_del.delete()
    return redirect(color)


def brand(request):
    brand_dict = {
        'band': Brand.objects.all(),
    }

    return render(request, "admin_side/brand.html", brand_dict)


def brand_edit(request, id):
    if request.method == 'POST':

        band_name = request.POST['b_name']
        slug = request.POST['slug']

        band_update = Brand.objects.get(id=id)
        band_image = request.FILES['b_image']

        band_update.brand_image = band_image
        band_update.save()

        band_update = Brand.objects.filter(id=id)
        band_update.update(brand_name=band_name, slug=slug)
        return redirect(brand)

    return render(request, "admin_side/brand.html")

# brand add


def brand_add(request):

    band_name = request.POST['b_name']
    band_image = request.FILES['b_image']
    slug = request.POST['slug']

    band_add = Brand.objects.create(
        brand_name=band_name, brand_image=band_image, slug=slug)
    band_add.save()

    return redirect(brand)

# brand delete


def brand_delete(request, id):
    del_band = Brand.objects.filter(id=id)
    del_band.delete()
    return redirect(brand)


def banner(request):
    banner = Banner.objects.all()
    context = {
        'banner': banner
    }

    return render(request, "admin_side/banner.html", context)


def banner_delete(request, id):
    del_ban = Banner.objects.filter(id=id)
    del_ban.delete()
    return redirect(banner)


def banner_add(request):

    bann_name = request.POST['b_name']
    bann_description = request.POST['b_description']
    bann_image = request.FILES['b_image']

    bann_add = Banner.objects.create(
        heading=bann_name, image=bann_image, description=bann_description)
    bann_add.save()

    return redirect(banner)


def banner_edit(request, id):
    if request.method == 'POST':

        bann_name = request.POST['b_name']
        bann_description = request.POST['b_description']

        image_update = Banner.objects.get(id=id)
        bann_image = request.FILES['b_image']

        image_update.image = bann_image
        image_update.save()

        bann_update = Banner.objects.filter(id=id)
        bann_update.update(heading=bann_name, description=bann_description)
        return redirect(banner)
    else:
        return render(request, "admin_side/banner.html")




def color_variant(request):
    product=Product.objects.all()
    varaint=Variation.objects.all()
    colr=Color.objects.all()
    context={
        'product':product,
        'varaint':varaint,
        'colr':colr    
        }
    return render(request,"admin_side/color_variant.html",context)

def varaint_add(request):
    if request.method=='POST':
        color=request.POST['color']
        product=request.POST['product']
        

        product_instance=Product.objects.get(id=product)
        color_intance=Color.objects.get(id=color)
        variant=Variation.objects.create(color=color_intance,product=product_instance)
        variant.save()
        return redirect(color_variant)
    else:
        return render(request,"admin_side/color_variant.html")

from django.http import Http404

def variant_edit(request,id):

    if request.method=='POST':
        color = request.POST['edit_color']

        color_instance = Color.objects.get(id=color)

        update_variant = Variation.objects.filter(id=id)
        
        update_variant.update(color=color_instance)

        return redirect(color_variant)
    
    else:

        return render(request, "admin_side/color_variant.html")


def varaint_delete(request,id):
    del_var= Variation.objects.filter(id=id)
    del_var.delete()
    return redirect(color_variant)




