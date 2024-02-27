
from ..models import Product
imgs = ["https://resnota.ru/upload/iblock/983/pelmeni_01.jpg",
            "https://orl.selhozproduct.ru/upload/usl/f_6254586527ec6.jpg",
            "https://meat-expert.ru/files/uploads/obzor/_2023/30/01.jpg"]
products = [Product(1,150.0,"Медвежье ухо","Пельмени вкусные",imgs[0]),
            Product(2,250.0,"Вятское ухо","Пельмени вкусные",imgs[1]),
            Product(3,100.0,"Татарские","Пельмени вкусные",imgs[2])]
def GetAllProducts()->list:


    print("Подключились к базе данных достали все товары")
    return products
def FindProductById(id:int) -> Product:
    for product in products:
        if product.id == id:
            return product

