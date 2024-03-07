from ..models import Cart
import mainApp.services.productService as PS
cart = Cart()
cart.summ = 0.0
cart.save()
products = []
def GetCart():
    return cart

def AddProductInCart(id):
    product = PS.FindProductById(id)
    cart.summ += product.price
    cart.products.add(product)

def GetProductsInCart():
    productsTemp = cart.products.all().values_list()
    products = []
    for item in list(productsTemp):
        products.append(PS.FindProductById(item[0]))
    return products

def GetSum():
    return cart.summ

def GetCheck():
    message = ""
    message = f"номер заказа{cart.id}\n"
    for product in GetProductsInCart():
        message += f"{product.name} : {product.price} Руб.\n"
    message += f"Итог: {cart.summ}"
    return message

