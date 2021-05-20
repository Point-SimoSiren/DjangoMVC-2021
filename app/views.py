from django.shortcuts import render, redirect
from .models import Supplier, Product

def landingview(request):
    return render (request, 'landingpage.html')

# SUPPLIERS

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request,"suppliers.html",context)

def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def deletesupplier(request, id):
    Supplier.objects.filter(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])

# PRODUCTS

def productlistview(request):
    productlist = Product.objects.all()
    context = {'products': productlist}
    return render (request,"products.html",context)


def addproduct(request):
    a = request.POST['productname']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['companyname']
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, companyname = e).save()
    return redirect(request.META['HTTP_REFERER']) 