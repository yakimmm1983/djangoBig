from django.shortcuts import render,redirect
from mainApp.services.productService import GetAllProducts,FindProductById
from mainApp.services.toppingService import GetAllTopping
from mainApp.services.cartService import GetCart as GC,AddProductInCart


def Main(request):
    products = GetAllProducts()
    return render(request,'index.html',{'products':products})

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
        "products":cart.GetProducts(),
        "summ":cart.GetSum()
    }
    return render(request,'cart.html',contex)


