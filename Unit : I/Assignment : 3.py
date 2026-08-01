#Assignment : 3
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price):
        pass



class NoDiscount(DiscountStrategy):
    def apply(self, price):
        print(f"No discount applied. Final price: ${price}")


class FestiveDiscount(DiscountStrategy):
    def apply(self, price):
        final = price - (price * 0.2)
        print(f"Festive discount applied. Final price: ${final}")


class StudentDiscount(DiscountStrategy):
    def apply(self, price):
        final = price - (price * 0.1)
        print(f"Student discount applied. Final price: ${final}")


class BillingSystem:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def generate_bill(self, price):
        if self.strategy is None:
            print("Please select a discount type.")
        else:
            self.strategy.apply(price)


billing = BillingSystem()

while True:
    print("\n===== Billing System =====")
    print("1. No Discount")
    print("2. Festive Discount")
    print("3. Student Discount")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank you for shopping with us!")
        break

    price = float(input("Enter price: "))

    if choice == 1:
        billing.set_strategy(NoDiscount())
    elif choice == 2:
        billing.set_strategy(FestiveDiscount())
    elif choice == 3:
        billing.set_strategy(StudentDiscount())
    else:
        print("Invalid choice!")
        continue

    billing.generate_bill(price)

#Output
'''===== Billing System =====
1. No Discount
2. Festive Discount
3. Student Discount
4. Exit
Enter your choice: 2
Enter price: 1000
Festive discount applied. Final price: $800.0

===== Billing System =====
1. No Discount
2. Festive Discount
3. Student Discount
4. Exit
Enter your choice: 3
Enter price: 500
Student discount applied. Final price: $450.0

===== Billing System =====
1. No Discount
2. Festive Discount
3. Student Discount
4. Exit
Enter your choice: 4
Thank you for shopping with us!'''