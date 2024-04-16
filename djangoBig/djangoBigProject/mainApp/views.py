from django.shortcuts import render,redirect
from mainApp.services.productService import GetAllProducts,FindProductById
from mainApp.services.toppingService import GetAllTopping
from mainApp.services.cartService import GetCart as GC,AddProductInCart,GetCheck,GetProductsInCart,GetSum
from mainApp.EmailSander import EmailSender
from mainApp.forms import UserRegisterForm
def Main(request):
    products = GetAllProducts()
    return render(request,'index.html',{'products':products})
def RedirectMain(request):
    return redirect('main')

def Product(request,product_id):
    product = FindProductById(product_id)
    toppings = GetAllTopping()
    return render(request,'product.html',{"product":product,"toppings":toppings})

def AddInCart(request,product_id):
    AddProductInCart(product_id)
    return redirect('main')

def GetCart(request):
    cart = GC()
    contex = {
        "products":GetProductsInCart(),
        "summ":GetSum()
    }
    return render(request,'cart.html',contex)

def SendEmail(request):
    if request.method == "POST":
        email = request.POST.get("email")
        cart = GC()
        cart.save()
        message = GetCheck()
        emailSender = EmailSender(email)
        emailSender.SendEmail("Заказ",message)
    return redirect("main")

def register(request):
    from django.contrib import messages
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,"Вы успешно зарегистрировались")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'registration.html',{'reg_form':form})


