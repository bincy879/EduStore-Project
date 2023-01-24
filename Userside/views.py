from django.shortcuts import render,redirect
from Adminside.models import category_db,product_db,contact_db
from Userside.models import reg_db,cart_db
# Create your views here.
def home(request):
    data=category_db.objects.all()
    return render(request,"homepage.html",{'data':data})

def about(request):
    data = category_db.objects.all()
    return render(request,"About.html",{'data':data})

def products(request):
    data=category_db.objects.all()
    return render(request,"products.html",{'data':data})

def disPdt(request,itemCatg):
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    data=category_db.objects.all()
    products=product_db.objects.filter(Category=itemCatg)
    context={
        'products':products,
        'catg':catg,
        'data':data
    }
    return render(request,"dis_pdt.html",context)

def show_pdt(request,dataid):
    dat=product_db.objects.get(id=dataid)
    data = category_db.objects.all()
    return render(request,"show_product.html",{'dat':dat,'data':data})

def reg(request):
    return render(request,"registration.html")

def reg_save(request):
    if request.method=="POST":
        us=request.POST.get('usr')
        em=request.POST.get('e_id')
        pd=request.POST.get('pswd')
        cpd=request.POST.get('c_pwd')
        if pd==cpd:
            obj=reg_db(Username=us,Email=em,Password=pd,C_Password=cpd)
            obj.save()
            return redirect(reg)
        else:
            return render(request,"registration.html",{'msg':"Incorrect password!!"})

def login(request):
    return render(request,"log.html")

def log_save(request):
    if request.method=="POST":
        us=request.POST.get('user')
        pd=request.POST.get('pswd')
        if reg_db.objects.filter(Username=us,Password=pd).exists():
            request.session['user']=us
            request.session['pswd']=pd

            return redirect(home)
        else:
            return render(request,"log.html",{'msg':"Invalid username and password!!"})
    else:
        return redirect(home)

def logout(request):
    del request.session['user']
    del request.session['pswd']
    return redirect(home)

def contact(request):
    data = category_db.objects.all()
    return render(request,"contact.html",{'data':data})

def msg_save(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email_id')
        su=request.POST.get('subj')
        ms=request.POST.get('mesg')
        obj=contact_db(Name=na,Email=em,Sub=su,Msg=ms)
        obj.save()
        return redirect(contact)
