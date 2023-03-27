from django.shortcuts import render,redirect
from product.models import Category

# Create your views here.

def category(request):
    category_dict = {
        'catg': Category.objects.all(),
    }
    return render(request,"admin_side/categories.html",category_dict)

def category_edit(request,id):

    cat_name = request.POST['category_name']
    slug = request.POST['slug']
    cat_update = Category.objects.filter(id=id)

    cat_update.update(category_name=cat_name,slug=slug)

    return redirect(category)



def category_add(request):
    if request.method == 'POST':

        name = request.POST['cat_name']
        slug = request.POST['slug']

        cat_add = Category.objects.create(category_name=name,slug=slug)
        cat_add.save()

        return redirect(category)

    else:
        return render(request, "admin_side/categories.html")
    


def category_delete(request, id):
    del_cat = Category.objects.filter(id=id)
    del_cat.delete()
    return redirect(category)
