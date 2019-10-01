from time import sleep

class Restaurant():    
        
    def __new__(cls, *args, **kwargs):
        print(f"Restaurant.__new__:{args}")
        if not hasattr(cls, "_instance"):
            print("Creating new single instance")
            cls._instance = super(Restaurant, cls).__new__(cls, *args, **kwargs)
            cls._instance._order=0
            cls._instance._total_sales=0
        else:
            print("Using existing instance")
        return cls._instance
        
    def __init__(self):
        pass
            
 
    def __str__(self):
        return f"This restaurant had {self._order} orders today for a total of ${self._total_sales} in sales"
        
    def order_food(self, food_type):
        if food_type=="cheeseburger":
            Food.order_food("Cheeseburger")
            self._order = self._order + 1
            self._total_sales = (self._total_sales) + Cheeseburger().price()
        elif food_type=="pasta":
            Food.order_food("Pasta")
            self._order = self._order + 1
            self._total_sales = (self._total_sales) + Pasta().price()
        elif food_type=="pizza":
            Food.order_food("Pizza")
            self._order = self._order + 1
            self._total_sales = (self._total_sales) + Pizza().price()
    

class Food(object):
    def __init__(self):
        pass
        
    def price(self):
        return 0
        
    def prepare(self):
        pass
    
    @staticmethod    
    def order_food(food_type):
        if food_type.lower() == "cheeseburger":
            food = Cheeseburger()
            food.prepare()
        elif food_type.lower() == "pasta":
            food = Pasta()
            food.prepare()
        elif food_type.lower() == "pizza":
            food = Pizza()
            food.prepare()
        
        
class Cheeseburger(Food):
    def __str__(self):
        return f"{__class__.__name__}: {__class__.price(self)}"
        
    def price(self):
         return 5.99
        
    def prepare(self):
        print("Cheeseburger: grill all-beef patty")
        sleep(2)
        print("Cheeseburger: flip patty")
        sleep(2)
        print("Cheeseburger: put cheese on patty")
        sleep(2)
        print("Cheeseburger: put patty on bun and add toppings")
        sleep(2)
        print("Cheeseburger: All done!")
        sleep(2)
        print(Cheeseburger())
        sleep(2)
        
class Pasta(Food):
    def __str__(self):
        return f"{__class__.__name__}: {__class__.price(self)}"
        
    def price(self):
        return 4.99
        
    def prepare(self):
        print("Pasta: boil water for noodles")
        sleep(2)
        print("Pasta: saute onions, garlic and tomatoes for sauce")
        sleep(2)
        print("Pasta: put noodles in water")
        sleep(2)
        print("Pasta: season the sauce")
        sleep(2)
        print("Pasta: plate noodles and add sauce on top")
        sleep(2)
        print("Pasta: All done!")
        sleep(2)
        print(Pasta())
        sleep(2)
     
class Pizza(Food):
    def __str__(self):
        return f"{__class__.__name__}: {__class__.price(self)}"
        
    def price(self):
        return 2.99
        
    def prepare(self):
        print("Pizza: preparing the dough")
        sleep(2)
        print("Pizza: putting topping onto the dough")
        sleep(2)
        print("Pizza: baking pizza")
        sleep(2)
        print("Pizza: putting Pizza in a box")
        sleep(2)
        print("Pizza: All done!")
        sleep(2)
        print(Pizza())
        sleep(2)
        

        
        
def main():
    r = Restaurant()
    food = r.order_food("cheeseburger")
    if food:
        print(food)

    food = r.order_food("pasta")
    if food:
        print(food)

    food = r.order_food("mac and cheese") # doesn't exist, prints failure message
    if food:
        print(food)
    else:
        print("Sorry, the restaurant does not make 'mac and cheese'")
    print(r) 
    
    r2 = Restaurant()
    food = r.order_food("pasta")
    if food:
        print(food)
        
    food = r.order_food("pizza")
    if food:
        print(food)
    print(r2)
        
if __name__ == "__main__":
    main() 