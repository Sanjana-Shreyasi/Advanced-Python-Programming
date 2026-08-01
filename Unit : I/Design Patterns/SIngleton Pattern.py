#Design Pattern
#Singleton Pattern

class PrinterManager():
    _instance = None

    def __new__(cls):
        if cls._instance is None:  # Check if an instance already exists
            cls._instance = super().__new__(cls)
            print("Initializing Printer Manager!")
        return cls._instance


printer1 = PrinterManager()
printer2 = PrinterManager()

print(printer1 is printer2)

# Output 
'''Initializing Printer Manager!
True'''