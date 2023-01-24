from django.shortcuts import render,redirect
from Adminside.models import admin_db,category_db,product_db,contact_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def indexfn(request):
    return render(request,"index.html")

def add_admin(request):
    return render(request,"add_admin.html")

def save_admin(request):
    if request.method=="POST":
        na=request.POST.get('a_name')
        em=request.POST.get('a_email')
        mo=request.POST.get('a_mob')
        im=request.FILES['a_img']
        ad=request.POST.get('a_adrss')
        obj=admin_db(Name=na,Email_id=em,Mobile=mo,Image=im,Address=ad)
        obj.save()
        return redirect(add_admin)

def view_admin(request):
    data=admin_db.objects.all()
    return render(request,"view_admin.html",{'data':data})

def edit_admin(request,dataid):
    data=admin_db.objects.get(id=dataid)
    print(data)
    return render(request,"edit_admin.html",{'data':data})

def update_admin(request,dataid):
    if request.method=="POST":
        na=request.POST.get('a_name')
        em=request.POST.get('a_email')
        mo=request.POST.get('a_mob')
        ad = request.POST.get('a_adrss')
        try:
            im = request.FILES['a_img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=admin_db.objects.get(id=dataid).Image
        admin_db.objects.filter(id=dataid).update(Name=na,Email_id=em,Mobile=mo,Image=file,Address=ad)
        return redirect(view_admin)

def del_admin(request,dataid):
    data=admin_db.objects.filter(id=dataid)
    data.delete()
    return redirect(view_admin)
def add_catgry(request):
    return render(request,"add_category.html")

def save_catgry(request):
    if request.method=="POST":
        na=request.POST.get('c_name')
        de=request.POST.get('c_desc')
        im=request.FILES['c_img']
        obj=category_db(C_Name=na,Descr=de,C_Image=im)
        obj.save()
        return redirect(add_catgry)

def view_catgry(request):
    data=category_db.objects.all()
    return render(request,"view_category.html",{'data':data})

def edit_category(request,dataid):
    data=category_db.objects.get(id=dataid)
    print(data)
    return render(request,"edit_category.html",{'data':data})

def update_category(request,dataid):
    if request.method=="POST":
        na=request.POST.get('c_name')
        de=request.POST.get('c_desc')
        try:
            im = request.FILES['c_img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=category_db.objects.get(id=dataid).C_Image
        category_db.objects.filter(id=dataid).update(C_Name=na,Descr=de,C_Image=file)
        return redirect(view_catgry)

def del_category(request,dataid):
    data=category_db.objects.filter(id=dataid)
    data.delete()
    return redirect(view_catgry)

def add_product(request):
    data=category_db.objects.all()
    return render(request,"add_products.html",{'data':data})

def save_pdt(request):
    if request.method=="POST":
        na=request.POST.get('p_name')
        de=request.POST.get('p_desc')
        pr=request.POST.get('price')
        qy=request.POST.get('p_qty')
        ca=request.POST.get('category')
        im=request.FILES['p_img']
        obj=product_db(P_Name=na,Description=de,Price=pr,Quantity=qy,Category=ca,P_Img=im)
        obj.save()
        return redirect(add_product)

def view_product(request):
    data=product_db.objects.all()
    return render(request,"view_product.html",{'data':data})

def edit_product(request,dataid):
    data=product_db.objects.get(id=dataid)
    data1=category_db.objects.all()
    print(data)
    return render(request,"edit_product.html",{'data':data,'data1':data1})

def update_product(request,dataid):
    if request.method=="POST":
        na=request.POST.get('p_name')
        de=request.POST.get('p_desc')
        pr = request.POST.get('price')
        qy = request.POST.get('p_qty')
        ca=request.POST.get('category')
        try:
            im = request.FILES['p_img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=product_db.objects.get(id=dataid).P_Img
        product_db.objects.filter(id=dataid).update(P_Name=na,Description=de,Price=pr,Quantity=qy,Category=ca,P_Img=file)
        return redirect(view_product)

def del_product(request,dataid):
    data=product_db.objects.filter(id=dataid)
    data.delete()
    return redirect(view_product)

def login_page(request):
    return render(request,"login.html")

def session(request):
    if request.method=="POST":
        username_r=request.POST.get('user')
        password_r=request.POST.get('pswd')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['user']=username_r
                request.session['pswd']=password_r
                return redirect(indexfn)
            else:
                return redirect(login_page)
        else:
            return redirect(login_page)

def log_out(request):
    del request.session['user']
    del request.session['pswd']
    return redirect(indexfn)

def view_msg(request):
    data=contact_db.objects.all()
    return render(request,"view_msg.html",{'data':data})

def del_msg(request,dataid):
    data=contact_db.objects.filter(id=dataid)
    data.delete()
    return redirect(view_msg)