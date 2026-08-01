# Base class
class Drink:
    def make(self):
        print("Making drink...")


# Concrete classes
class Coffee(Drink):
    def make(self):
        print("Making Coffee")


class Tea(Drink):
    def make(self):
        print("Making Tea")


class Juice(Drink):
    def make(self):
        print("Making Juice")


# Factory class
class DrinkFactory:
    @staticmethod
    def get_drink(drink_type):
        if drink_type == "coffee":
            return Coffee()
        elif drink_type == "tea":
            return Tea()
        elif drink_type == "juice":
            return Juice()
        else:
            return None


# Client code
drink_type = input("Enter drink type: ").lower()
drink = DrinkFactory.get_drink(drink_type)

if drink:
    drink.make()
else:
    print("Drink not available")

# Output 
'''Enter drink type: Tea
Making Tea'''