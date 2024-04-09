from ..models import Topping


# toppings = [Topping(1,"Кетчуп",30.0),
#             Topping(2,"Сметана",30.0)]
def GetAllTopping() -> Topping:
    return Topping.objects.all()





