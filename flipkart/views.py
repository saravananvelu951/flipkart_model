from django.shortcuts import render, HttpResponse , redirect

from .models import *

from django.contrib.auth.hashers import make_password,check_password

def index(request):
    if request.method == 'POST':
        product_id = request.POST.get("productid")
        remove = request.POST.get("remove")
        print(product_id)

        cart_id = request.session.get("cart")  
        print(cart_id)
        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                 if remove:
                    if quantity <= 1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
            
                 else:
                    cart_id[product_id]=quantity + 1
            else:
                cart_id[product_id] = 1
                
        else:
            cart_id ={}
            cart_id[product_id] = 1
        request.session['cart'] = cart_id
        print(request.session['cart'])

    category_obj = category.objects.all()
    
    category_id = request.GET.get("category_id")

    search = request.GET.get("search")

    
    if category_id:
        product_obj = product.objects.filter(product_category=category_id)
    elif search:
        product_obj = product.objects.filter(product_name__icontains=search)
        #product_obj = product.objects.filter(product_name__iexact=search)

    else:
        product_obj = product.objects.all()

    context={
        'category':category_obj,
        'product': product_obj
 
    }
    return render(request,'home.html',context=context)

def sign_up(request):
    if request.method == "POST":
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile_num = request.POST.get('number')
        gender = request.POST.get('gender')

        class_obj = Registration (
            First_name = f_name,
            Last_name  = l_name,
            email   = email,
            password   = make_password(password),
            Mobile     = mobile_num,
            gender     = gender
        )
        class_obj.save()

        return redirect('homepage')
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

    try:
        email_id = Registration.objects.get(email=email)
        if check_password(password, email_id.password):
            request.session['name'] = email_id.First_name
            request.session['customer_id'] = email_id.id

            return redirect ("homepage")
        else:
         return HttpResponse("password wrong")
    
    except:
        return HttpResponse("mail not found ")

def logout(request):
    request.session.clear()
    return redirect ("homepage")

def cart_details(request):
    cart_id = list(request.session.get("cart").keys())
    Product = product.objects.filter(id__in = cart_id)

    context={
        "product": Product
        }
    return render(request, "cart.html",context=context)

def checkout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer_id =request.session.get('customer_id')
        if not customer_id:
            return HttpResponse("please login")
        cart_id = request.session.get('cart')
        Product = product.objects.filter(id__in= list(cart_id.keys()))
        
        for pro in Product:
            order_obj = Order(
                
                address  = address,
                mobile = mobile,
                customer = Registration(id=customer_id),
                product = pro,
                quantity = cart_id.get(str(pro.id)),
                price = pro.product_price
            )
            order_obj.save()
        return redirect("order")

def order_details(request):
    customer_id =request.session.get('customer_id')
    order = Order.objects.filter(customer=customer_id)
    total_price = 0
    for i in order:
        total_price = total_price + i.price * i.quantity

    context ={
        "order": order,
        "total_price": total_price
    }
    
    return render(request,"order.html",context=context)

from rest_framework import  viewsets

from .serializers import RegistrationSerializer

class registrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer 

def contact(request):
    
    return render(request,'cont.html')


