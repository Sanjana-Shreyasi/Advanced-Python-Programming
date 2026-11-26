#PBA 3
#Section A 
#Problem 1
#Hotel Order 

class Order:
    def __init__(self,customer_name,food_item,order_amount,veg,non_veg):
        self.customer_name=customer_name
        self.food_item=food_item
        self.order_amount=order_amount
        self.veg=veg
        self.non_veg=non_veg

    def display(self):
        print("Order details:")
        print("Customer name:",self.customer_name)
        print("Food item:",self.food_item)
        print("Order amount:",self.order_amount)
        if self.veg==1:
            print("Veg item")
        elif self.non_veg==1:
            print("Non veg item")


class Restraunt:
    def __init__(self):
        self.order=[]

    def Add_Order(self,order):
        self.order.append(order)

    def display(self):
        for i in self.order:
            i.display()
            

o1=Order("Nitin Sharma","Spring Roll",200,1,0)
o2=Order("Rahul Sharma","Chicken soup",400,0,1)   

restraunt=Restraunt()
restraunt.Add_Order(o1)
restraunt.Add_Order(o2)
restraunt.display()

#Output
'''Order details:
Customer name: Nitin Sharma
Food item: Spring Roll
Order amount: 200
Veg item
Order details:
Customer name: Rahul Sharma
Food item: Chicken soup
Order amount: 400
Non veg item'''
